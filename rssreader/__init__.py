import functools

import json

from flask import Flask, render_template, jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from rssreader.helpers import accept

app = Flask(__name__)
app.config.from_object('config')
CORS(app)

db = SQLAlchemy(app)

from rssreader.models import Feed

@app.errorhandler(HTTPException)
@accept
def handle_exception(e):
    return e

@app.errorhandler(HTTPException)
@handle_exception.accept('application/json')
def handle_exception_json(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "status": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

@app.route('/', methods=['GET'])
@accept
def root():
    return render_template("root.html")

@root.accept('application/json')
def root_json():
    return jsonify({})

@app.route('/feeds', methods=['GET', 'POST'])
@accept
def feeds():
    if request.method != "GET":
        return error("With the given content-type, only GET is allowed", asJSON=False)
    return render_template("todo.html")

@feeds.accept('application/json')
def feeds_json():
    if request.method == 'GET':
        return jsonify([x.json() for x in Feed.query.all()])
    elif request.method == 'POST':
        new_feed = request.get_json()
        if 'name' not in new_feed or new_feed['name'] == '':
            return error("Missing field 'name'")
        if 'url' not in new_feed or new_feed['url'] == '':
            return error("Missing field 'url'")
        feed = Feed()
        feed.name = new_feed['name']
        feed.url = new_feed['url']
        db.session.add(feed)
        db.session.commit()
        return jsonify(feed.json())

@app.route('/feeds/<int:feedId>', methods=["GET", "DELETE", "PATCH"])
@accept
def feed_by_id(feedId):
    if request.method != "GET":
        return error("With the given content-type, only GET is allowed", asJSON=False)
    feed = Feed.query.get_or_404(feedId)
    return render_template("todo.html")

@feed_by_id.accept('application/json')
def feed_by_id_json(feedId):
    feed = Feed.query.get_or_404(feedId)
    if request.method == 'GET':
        return jsonify(feed.json())
    elif request.method == 'DELETE':
        db.session.delete(feed)
        db.session.commit()
        return "", 204
    elif request.method == 'PATCH':
        patch = request.json
        if "name" in patch:
            feed.name = patch["name"]
        if "description" in patch:
            feed.description = patch["description"]
        if "priority" in patch:
            feed.priority = patch["priority"]
        if "hidden" in patch:
            feed.hidden = patch["hidden"]
        db.session.add(feed)
        db.session.commit()
        return jsonify(feed.json())

def error(description, status=400, asJSON=True):
    if asJSON:
        return jsonify({
            'status': status,
            'detail': description
            }), status
    return render_template("error.html", status=status, description=description)

db.create_all()
