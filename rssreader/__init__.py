import functools

import json

from flask import Flask, render_template, jsonify, g, current_app
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

from rssreader.helpers import accept

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
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

        from rssreader import feeds
        from rssreader import posts

        app.register_blueprint(feeds.bp)
        app.register_blueprint(posts.bp)

        db.init_app(app)
        db.create_all()

    return app
