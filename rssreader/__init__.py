"""
rssreader: The main Flask rssreader
"""

# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    """
    not_found: Handles HTTP error code 404 Not Found
    """
    return render_template('404.html', error=error), 404


# Set the route and accepted methods
@app.route('/', methods=['GET'])
def root():
    """
    root: The root route
    """
    return render_template("root.html")


# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
