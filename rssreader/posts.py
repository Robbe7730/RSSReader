from rssreader import get_db

from rssreader.models import Post
from rssreader.helpers import accept, error

from flask import render_template, request, Blueprint, jsonify

bp = Blueprint('posts', __name__, url_prefix='/posts')

db = get_db

@bp.route('/', methods=['GET'])
@accept
def posts():
    return render_template("todo.html")

@posts.accept('application/json')
def posts_json():
    return jsonify([x.json() for x in Post.query.all()])

@bp.route('/<int:postId>', methods=['GET', 'DELETE', 'PATCH'])
@accept
def post_by_id(postId):
    if request.method != 'GET':
        return error("With the given content-type, only GET is allowed", asJSON=False)
    return render_template("todo.html")

@post_by_id.accept("application/json")
def post_by_id_json(postId):
    post = Post.query.get_or_404(postId)
    if request.method == 'GET':
        return jsonify(post.json())
    elif request.method == 'DELETE':
        db.session.delete(post)
        db.session.commit()
        return "", 204
    elif request.method == 'PATCH':
        patch = request.json
        if patch is None:
            return error("No patch provided", 400)
        if "title" in patch:
            post.title = patch["title"]
        if "description" in patch:
            post.title = patch["description"]
        if "link" in patch:
            post.link = patch["link"]
        if "read" in patch:
            post.read = patch["read"]
        if "feed" in patch:
            post.feed = patch["feed"]
        db.session.add(post)
        db.session.commit()
        return jsonify(post.json())
