import functools

import json

from flask import Flask, render_template, jsonify, g
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from rssreader.helpers import accept

def get_db():
    return g.db

def create_db(app):
    g.db = SQLAlchemy(app)
    g.db.create_all()

def create_app():

    app = Flask(__name__)
    app.config.from_object('config')
    CORS(app)

    @app.errorhandler(HTTPException)
    @accept
    def handle_exception(e):
        return e

    @app.errorhandler(HTTPException)
    @handle_exception.accept('application/json')
    def handle_exception_json(e):
        response = e.get_response()
        response.data = json.dumps({
            "status": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response, e.code

    @app.route('/', methods=['GET'])
    @accept
    def root():
        return render_template("root.html")

    @root.accept('application/json')
    def root_json():
        return jsonify({})

    with app.app_context():
        create_db(app)

        import rssreader.feeds as feeds
        app.register_blueprint(feeds.bp)

        import rssreader.posts as posts
        app.register_blueprint(posts.bp)

    return app
