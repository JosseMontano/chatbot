from flask_sqlalchemy import SQLAlchemy
from .db import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    patterns = db.relationship("Pattern", backref="tag", lazy=True)
    responses = db.relationship("Response", backref="tag", lazy=True)

    def __repr__(self):
        return f"<Tag {self.name}>"
