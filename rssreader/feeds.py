from rssreader import get_db

from rssreader.models import Feed
from rssreader.helpers import accept, error

from flask import render_template, request, Blueprint, jsonify

bp = Blueprint('feeds', __name__, url_prefix='/feeds')

db = get_db()

@bp.route('/', methods=['GET', 'POST'])
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

@bp.route('/<int:feedId>', methods=["GET", "DELETE", "PATCH"])
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

@bp.route('/<int:feedId>/posts', methods=["GET"])
@accept
def posts_for_feed(feedId):
    feed = Feed.query.get_or_404(feedId)
    return render_template("todo.html")

@posts_for_feed.accept('application/json')
def posts_for_feed_json(feedId):
    feed = Feed.query.get_or_404(feedId)
    return jsonify([post.json() for post in feed.posts])
