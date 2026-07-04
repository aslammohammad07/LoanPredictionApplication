from extensions import db
from models.applicant import Applicant
from models.loan import LoanApplication
from sqlalchemy import asc, desc, or_
from utils.logger import logger


def create_applicant(data, user_id):

    applicant = Applicant(
        user_id=user_id,
        gender=data["gender"].capitalize(),
        married=data["married"].capitalize(),
        dependents=data["dependents"],
        education=data["education"].capitalize(),
        self_employed=data["self_employed"].capitalize(),
        property_area=data["property_area"].capitalize()
    )

    db.session.add(applicant)
    db.session.commit()

    logger.info(
        f"Applicant created. Applicant ID: {applicant.applicant_id}, User ID: {user_id}"
    )

    return {
        "success": True,
        "message": "Applicant profile created successfully.",
        "applicant_id": applicant.applicant_id
    }, 201


def get_applicant(applicant_id):

    applicant = db.session.get(Applicant, applicant_id)

    if applicant is None:

        logger.warning(
            f"Applicant not found. Applicant ID: {applicant_id}"
        )

        return {
            "success": False,
            "message": "Applicant not found."
        }, 404

    logger.info(
        f"Applicant viewed. Applicant ID: {applicant_id}"
    )

    return {
        "success": True,
        "data": {
            "applicant_id": applicant.applicant_id,
            "user_id": applicant.user_id,
            "gender": applicant.gender,
            "married": applicant.married,
            "dependents": applicant.dependents,
            "education": applicant.education,
            "self_employed": applicant.self_employed,
            "property_area": applicant.property_area
        }
    }, 200


def get_all_applicants(page, size, search, sort_by, order):

    query = Applicant.query

    if search:
        query = query.filter(
            or_(
                Applicant.gender.ilike(f"%{search}%"),
                Applicant.education.ilike(f"%{search}%"),
                Applicant.property_area.ilike(f"%{search}%"),
                Applicant.married.ilike(f"%{search}%"),
                Applicant.self_employed.ilike(f"%{search}%")
            )
        )

    if hasattr(Applicant, sort_by):

        if order.lower() == "desc":
            query = query.order_by(
                desc(getattr(Applicant, sort_by))
            )
        else:
            query = query.order_by(
                asc(getattr(Applicant, sort_by))
            )

    pagination = query.paginate(
        page=page,
        per_page=size,
        error_out=False
    )

    applicants = []

    for applicant in pagination.items:

        applicants.append({
            "applicant_id": applicant.applicant_id,
            "user_id": applicant.user_id,
            "gender": applicant.gender,
            "married": applicant.married,
            "dependents": applicant.dependents,
            "education": applicant.education,
            "self_employed": applicant.self_employed,
            "property_area": applicant.property_area
        })

    logger.info(
        f"Applicants retrieved. Total: {pagination.total}"
    )

    return {
        "success": True,
        "page": pagination.page,
        "size": pagination.per_page,
        "total_records": pagination.total,
        "total_pages": pagination.pages,
        "data": applicants
    }, 200


def update_applicant(applicant_id, data):

    applicant = db.session.get(Applicant, applicant_id)

    if applicant is None:

        logger.warning(
            f"Update failed. Applicant not found. Applicant ID: {applicant_id}"
        )

        return {
            "success": False,
            "message": "Applicant not found."
        }, 404

    applicant.gender = data["gender"].capitalize()
    applicant.married = data["married"].capitalize()
    applicant.dependents = data["dependents"]
    applicant.education = data["education"].capitalize()
    applicant.self_employed = data["self_employed"].capitalize()
    applicant.property_area = data["property_area"].capitalize()

    db.session.commit()

    logger.info(
        f"Applicant updated. Applicant ID: {applicant_id}"
    )

    return {
        "success": True,
        "message": "Applicant updated successfully."
    }, 200


def patch_applicant(applicant_id, data):

    applicant = db.session.get(Applicant, applicant_id)

    if applicant is None:

        logger.warning(
            f"Partial update failed. Applicant not found. Applicant ID: {applicant_id}"
        )

        return {
            "success": False,
            "message": "Applicant not found."
        }, 404

    if "gender" in data:
        applicant.gender = data["gender"].capitalize()

    if "married" in data:
        applicant.married = data["married"].capitalize()

    if "dependents" in data:
        applicant.dependents = data["dependents"]

    if "education" in data:
        applicant.education = data["education"].capitalize()

    if "self_employed" in data:
        applicant.self_employed = data["self_employed"].capitalize()

    if "property_area" in data:
        applicant.property_area = data["property_area"].capitalize()

    db.session.commit()

    logger.info(
        f"Applicant partially updated. Applicant ID: {applicant_id}"
    )

    return {
        "success": True,
        "message": "Applicant updated successfully."
    }, 200


def delete_applicant(applicant_id):

    applicant = db.session.get(Applicant, applicant_id)

    if applicant is None:

        logger.warning(
            f"Delete failed. Applicant not found. Applicant ID: {applicant_id}"
        )

        return {
            "success": False,
            "message": "Applicant not found."
        }, 404

    loan = LoanApplication.query.filter_by(
        applicant_id=applicant_id
    ).first()

    if loan:

        logger.warning(
            f"Delete blocked. Applicant ID: {applicant_id} has loan application(s)."
        )

        return {
            "success": False,
            "message": "Applicant cannot be deleted because loan application(s) exist."
        }, 400

    db.session.delete(applicant)
    db.session.commit()

    logger.info(
        f"Applicant deleted. Applicant ID: {applicant_id}"
    )

    return {
        "success": True,
        "message": "Applicant deleted successfully."
    }, 200