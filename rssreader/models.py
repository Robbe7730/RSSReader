"""
models.py: The SQLAlchemy models
"""

import rssreader

class Feed(rssreader.db.Model):
    __tablename__ = 'feed'
    id = rssreader.db.Column(rssreader.db.Integer, primary_key=True)
    name = rssreader.db.Column(rssreader.db.String(64), nullable=False)
    url = rssreader.db.Column(rssreader.db.String(128), nullable=False)
    priority = rssreader.db.Column(rssreader.db.Integer, nullable=True, default=1)
    hidden = rssreader.db.Column(rssreader.db.Boolean, default=False)
    posts = rssreader.db.relationship("Post")

    def __repr__(self):
        return '<Feed %r>' % self.name

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "priority": self.priority,
            "hidden": self.hidden
        }

class Post(rssreader.db.Model):
    __tablename__ = 'post'
    id = rssreader.db.Column(rssreader.db.Integer, primary_key=True)
    title = rssreader.db.Column(rssreader.db.String(32), nullable=False)
    description = rssreader.db.Column(rssreader.db.String(1024), nullable=False)
    link = rssreader.db.Column(rssreader.db.String(128), nullable=True)
    read = rssreader.db.Column(rssreader.db.Boolean, default=False)
    feed = rssreader.db.Column(rssreader.db.Integer, rssreader.db.ForeignKey('feed.id'))

    def __repr__(self):
        return '<Post %r>' % self.title
