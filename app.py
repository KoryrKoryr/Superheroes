#!/usr/bin/env python3

from flask import Flask
from flask_migrate import Migrate
from models import db


# Create Flask app instance
app = Flask(__name__)

# Configure the app with database URI and disable track modifications to reduce overhead
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Import routes to ensure they are registered with the app
from routes import *

db.init_app(app)

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
