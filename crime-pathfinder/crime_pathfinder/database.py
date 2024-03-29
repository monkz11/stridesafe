from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db = SQLAlchemy(app)

class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crime_type = db.Column(db.String(255))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    description = db.Column(db.Text)

# This line is not required as db.create_all() is called later in the script
# db.init_app(app)

with app.app_context():
    # Create tables
    db.create_all()