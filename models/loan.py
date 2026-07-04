from datetime import datetime, UTC

from extensions import db


class LoanApplication(db.Model):

    __tablename__ = "loan_application"

    loan_id = db.Column(
        db.Integer,
        primary_key=True
    )

    applicant_id = db.Column(
        db.Integer,
        db.ForeignKey("applicant_profile.applicant_id"),
        nullable=False
    )

    applicant_income = db.Column(
        db.Float,
        nullable=False
    )

    coapplicant_income = db.Column(
        db.Float,
        nullable=False,
        default=0
    )

    loan_amount = db.Column(
        db.Float,
        nullable=False
    )

    loan_term = db.Column(
        db.Integer,
        nullable=False
    )

    credit_history = db.Column(
        db.Integer,
        nullable=False
    )

    application_date = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC)
    )

    applicant = db.relationship(
        "Applicant",
        backref="loan_applications"
    )

    def __repr__(self):
        return f"<LoanApplication {self.loan_id}>"