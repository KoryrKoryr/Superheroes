from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create Flask app instance
app = Flask(__name__)

# Configure the app with database URI and disable track modifications to reduce overhead
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes to ensure they are registered with the app
from routes import *

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
