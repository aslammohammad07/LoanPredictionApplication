from sqlalchemy import asc, desc, or_

from extensions import db
from models.applicant import Applicant
from models.loan import LoanApplication
from models.prediction import Prediction

from ml.predict import predict_loan
from utils.logger import logger


def predict_loan_application(loan_id):

    loan = db.session.get(LoanApplication, loan_id)

    if loan is None:

        logger.warning(
            f"Prediction failed. Loan not found. Loan ID: {loan_id}"
        )

        return {
            "success": False,
            "message": "Loan application not found."
        }, 404

    applicant = db.session.get(Applicant, loan.applicant_id)

    if applicant is None:

        logger.warning(
            f"Prediction failed. Applicant not found. Applicant ID: {loan.applicant_id}"
        )

        return {
            "success": False,
            "message": "Applicant not found."
        }, 404

    model_input = {
        "Gender": applicant.gender,
        "Married": applicant.married,
        "Dependents": applicant.dependents,
        "Education": applicant.education,
        "Self_Employed": applicant.self_employed,
        "ApplicantIncome": loan.applicant_income,
        "CoapplicantIncome": loan.coapplicant_income,
        "LoanAmount": loan.loan_amount,
        "Loan_Amount_Term": loan.loan_term,
        "Credit_History": loan.credit_history,
        "Property_Area": applicant.property_area
    }

    prediction, probability = predict_loan(model_input)

    prediction_record = Prediction(
        loan_id=loan.loan_id,
        model_name="XGBoost",
        prediction=prediction,
        probability=probability
    )

    db.session.add(prediction_record)
    db.session.commit()

    logger.info(
        f"Prediction created. Prediction ID: {prediction_record.prediction_id}, Loan ID: {loan.loan_id}, Result: {prediction}"
    )

    return {
        "success": True,
        "prediction_id": prediction_record.prediction_id,
        "prediction": prediction,
        "probability": round(probability * 100, 2),
        "model": "XGBoost"
    }, 200


def get_prediction(prediction_id):

    prediction = db.session.get(Prediction, prediction_id)

    if prediction is None:

        logger.warning(
            f"Prediction not found. Prediction ID: {prediction_id}"
        )

        return {
            "success": False,
            "message": "Prediction not found."
        }, 404

    logger.info(
        f"Prediction viewed. Prediction ID: {prediction_id}"
    )

    return {
        "success": True,
        "data": {
            "prediction_id": prediction.prediction_id,
            "loan_id": prediction.loan_id,
            "model_name": prediction.model_name,
            "prediction": prediction.prediction,
            "probability": prediction.probability,
            "prediction_date": prediction.prediction_date
        }
    }, 200


def get_all_predictions(page, size, search, sort_by, order):

    query = Prediction.query

    if search:
        query = query.filter(
            or_(
                Prediction.model_name.ilike(f"%{search}%"),
                Prediction.prediction.ilike(f"%{search}%")
            )
        )

    if hasattr(Prediction, sort_by):

        if order.lower() == "desc":
            query = query.order_by(
                desc(getattr(Prediction, sort_by))
            )
        else:
            query = query.order_by(
                asc(getattr(Prediction, sort_by))
            )

    pagination = query.paginate(
        page=page,
        per_page=size,
        error_out=False
    )

    predictions = []

    for prediction in pagination.items:

        predictions.append({
            "prediction_id": prediction.prediction_id,
            "loan_id": prediction.loan_id,
            "model_name": prediction.model_name,
            "prediction": prediction.prediction,
            "probability": prediction.probability,
            "prediction_date": prediction.prediction_date
        })

    logger.info(
        f"Predictions retrieved. Total: {pagination.total}"
    )

    return {
        "success": True,
        "page": pagination.page,
        "size": pagination.per_page,
        "total_records": pagination.total,
        "total_pages": pagination.pages,
        "data": predictions
    }, 200


def delete_prediction(prediction_id):

    prediction = db.session.get(Prediction, prediction_id)

    if prediction is None:

        logger.warning(
            f"Delete failed. Prediction not found. Prediction ID: {prediction_id}"
        )

        return {
            "success": False,
            "message": "Prediction not found."
        }, 404

    db.session.delete(prediction)
    db.session.commit()

    logger.info(
        f"Prediction deleted. Prediction ID: {prediction_id}"
    )

    return {
        "success": True,
        "message": "Prediction deleted successfully."
    }, 200