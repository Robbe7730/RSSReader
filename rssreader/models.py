from rssreader import db

class Feed(db.Model):
    __tablename__ = 'feed'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    url = db.Column(db.String(128), nullable=False)
    priority = db.Column(db.Integer, nullable=True, default=1)
    hidden = db.Column(db.Boolean, default=False)
    posts = db.relationship("Post")

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

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    link = db.Column(db.String(128), nullable=True)
    read = db.Column(db.Boolean, default=False)
    feed = db.Column(db.Integer, db.ForeignKey('feed.id'), nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.title

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "link": self.link,
            "read": self.read,
            "feed": self.feed
        }
