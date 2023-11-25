from flask_sqlalchemy import SQLAlchemy
from .db import db

class Pattern(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(350), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"), nullable=False)

    def __repr__(self):
        return f"<Pattern {self.name}>"
