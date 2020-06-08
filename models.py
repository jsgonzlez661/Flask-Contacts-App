from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class contacts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fullname = db.Column(db.String(256))
	phone = db.Column(db.String(256))
	email = db.Column(db.String(256))
