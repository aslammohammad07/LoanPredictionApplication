from datetime import datetime, UTC

from extensions import db


class Prediction(db.Model):

    __tablename__ = "prediction_result"

    prediction_id = db.Column(
        db.Integer,
        primary_key=True
    )

    loan_id = db.Column(
        db.Integer,
        db.ForeignKey("loan_application.loan_id"),
        nullable=False
    )

    model_name = db.Column(
        db.String(100),
        nullable=False
    )

    prediction = db.Column(
        db.String(20),
        nullable=False
    )

    probability = db.Column(
        db.Float,
        nullable=False
    )

    prediction_date = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC)
    )

    loan = db.relationship(
        "LoanApplication",
        backref="predictions"
    )

    def __repr__(self):
        return f"<Prediction {self.prediction_id}>"