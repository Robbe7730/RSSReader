import functools

from flask import Flask, render_template, jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from rssreader.helpers import accept

app = Flask(__name__)
app.config.from_object('config')
CORS(app)

db = SQLAlchemy(app)

from rssreader.models import Feed

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error), 404

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


def error(description, status=400):
    return Response(description, status=status)

db.create_all()
