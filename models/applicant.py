from extensions import db


class Applicant(db.Model):

    __tablename__ = "applicant_profile"

    applicant_id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    gender = db.Column(
        db.String(20),
        nullable=False
    )

    married = db.Column(
        db.String(10),
        nullable=False
    )

    dependents = db.Column(
        db.String(10),
        nullable=False
    )

    education = db.Column(
        db.String(50),
        nullable=False
    )

    self_employed = db.Column(
        db.String(10),
        nullable=False
    )

    property_area = db.Column(
        db.String(50),
        nullable=False
    )

    user = db.relationship(
        "User",
        backref="applicants"
    )

    def __repr__(self):
        return f"<Applicant {self.applicant_id}>"