from sqlalchemy import asc, desc, or_
from extensions import db
from models.loan import LoanApplication
from models.prediction import Prediction
from utils.logger import logger


def create_loan(data):

    loan = LoanApplication(
        applicant_id=data["applicant_id"],
        applicant_income=data["applicant_income"],
        coapplicant_income=data["coapplicant_income"],
        loan_amount=data["loan_amount"],
        loan_term=data["loan_term"],
        credit_history=data["credit_history"]
    )

    db.session.add(loan)
    db.session.commit()

    logger.info(
        f"Loan created. Loan ID: {loan.loan_id}, Applicant ID: {loan.applicant_id}"
    )

    return {
        "success": True,
        "message": "Loan application submitted successfully.",
        "loan_id": loan.loan_id
    }, 201


def get_loan(loan_id):

    loan = db.session.get(LoanApplication, loan_id)

    if loan is None:

        logger.warning(
            f"Loan not found. Loan ID: {loan_id}"
        )

        return {
            "success": False,
            "message": "Loan application not found."
        }, 404

    logger.info(
        f"Loan viewed. Loan ID: {loan_id}"
    )

    return {
        "success": True,
        "data": {
            "loan_id": loan.loan_id,
            "applicant_id": loan.applicant_id,
            "applicant_income": loan.applicant_income,
            "coapplicant_income": loan.coapplicant_income,
            "loan_amount": loan.loan_amount,
            "loan_term": loan.loan_term,
            "credit_history": loan.credit_history,
            "application_date": loan.application_date
        }
    }, 200


def get_all_loans(page, size, search, sort_by, order):

    query = LoanApplication.query

    if search:
        query = query.filter(
            or_(
                LoanApplication.loan_amount.like(f"%{search}%"),
                LoanApplication.loan_term.like(f"%{search}%"),
                LoanApplication.credit_history.like(f"%{search}%")
            )
        )

    if hasattr(LoanApplication, sort_by):

        if order.lower() == "desc":
            query = query.order_by(
                desc(getattr(LoanApplication, sort_by))
            )
        else:
            query = query.order_by(
                asc(getattr(LoanApplication, sort_by))
            )

    pagination = query.paginate(
        page=page,
        per_page=size,
        error_out=False
    )

    loans = []

    for loan in pagination.items:

        loans.append({
            "loan_id": loan.loan_id,
            "applicant_id": loan.applicant_id,
            "applicant_income": loan.applicant_income,
            "coapplicant_income": loan.coapplicant_income,
            "loan_amount": loan.loan_amount,
            "loan_term": loan.loan_term,
            "credit_history": loan.credit_history,
            "application_date": loan.application_date
        })

    logger.info(
        f"Loans retrieved. Total: {pagination.total}"
    )

    return {
        "success": True,
        "page": pagination.page,
        "size": pagination.per_page,
        "total_records": pagination.total,
        "total_pages": pagination.pages,
        "data": loans
    }, 200


def update_loan(loan_id, data):

    loan = db.session.get(LoanApplication, loan_id)

    if loan is None:

        logger.warning(
            f"Update failed. Loan not found. Loan ID: {loan_id}"
        )

        return {
            "success": False,
            "message": "Loan application not found."
        }, 404

    loan.applicant_income = data["applicant_income"]
    loan.coapplicant_income = data["coapplicant_income"]
    loan.loan_amount = data["loan_amount"]
    loan.loan_term = data["loan_term"]
    loan.credit_history = data["credit_history"]

    db.session.commit()

    logger.info(
        f"Loan updated. Loan ID: {loan_id}"
    )

    return {
        "success": True,
        "message": "Loan application updated successfully."
    }, 200


def patch_loan(loan_id, data):

    loan = db.session.get(LoanApplication, loan_id)

    if loan is None:

        logger.warning(
            f"Partial update failed. Loan not found. Loan ID: {loan_id}"
        )

        return {
            "success": False,
            "message": "Loan application not found."
        }, 404

    if "applicant_income" in data:
        loan.applicant_income = data["applicant_income"]

    if "coapplicant_income" in data:
        loan.coapplicant_income = data["coapplicant_income"]

    if "loan_amount" in data:
        loan.loan_amount = data["loan_amount"]

    if "loan_term" in data:
        loan.loan_term = data["loan_term"]

    if "credit_history" in data:
        loan.credit_history = data["credit_history"]

    db.session.commit()

    logger.info(
        f"Loan partially updated. Loan ID: {loan_id}"
    )

    return {
        "success": True,
        "message": "Loan application updated successfully."
    }, 200


def delete_loan(loan_id):

    loan = db.session.get(LoanApplication, loan_id)

    if loan is None:

        logger.warning(
            f"Delete failed. Loan not found. Loan ID: {loan_id}"
        )

        return {
            "success": False,
            "message": "Loan application not found."
        }, 404

    prediction = Prediction.query.filter_by(
        loan_id=loan_id
    ).first()

    if prediction:

        logger.warning(
            f"Delete blocked. Loan ID: {loan_id} has prediction(s)."
        )

        return {
            "success": False,
            "message": "Loan cannot be deleted because prediction(s) exist."
        }, 400

    db.session.delete(loan)
    db.session.commit()

    logger.info(
        f"Loan deleted. Loan ID: {loan_id}"
    )

    return {
        "success": True,
        "message": "Loan deleted successfully."
    }, 200