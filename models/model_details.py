from datetime import datetime

from extensions import db


class ModelDetails(db.Model):

    __tablename__ = "model_details"

    model_id = db.Column(
        db.Integer,
        primary_key=True
    )

    model_name = db.Column(
        db.String(100),
        nullable=False
    )

    algorithm = db.Column(
        db.String(100),
        nullable=False
    )

    accuracy = db.Column(
        db.Float,
        nullable=False
    )

    version = db.Column(
        db.String(20),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<ModelDetails {self.model_name}>"