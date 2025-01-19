from datetime import datetime

from yacut import db
from .constants import MAX_LENGTH_SHORT


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(MAX_LENGTH_SHORT), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "original": self.original,
            "short_url": self.short,
            "timestamp": self.timestamp
        }
