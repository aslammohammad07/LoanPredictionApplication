from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from services.prediction_service import (
    predict_loan_application,
    get_prediction,
    get_all_predictions,
    delete_prediction
)

prediction_bp = Blueprint("prediction", __name__)


@prediction_bp.route("/predict", methods=["POST"])
@jwt_required()
def predict():
    """
    Predict Loan Application
    ---
    tags:
      - Prediction
    security:
      - Bearer: []
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - loan_id
          properties:
            loan_id:
              type: integer
              example: 1
    responses:
      200:
        description: Prediction generated successfully
      404:
        description: Loan not found
    """

    if not request.is_json:
        return {
            "success": False,
            "message": "Content-Type must be application/json"
        }, 415

    data = request.get_json()

    loan_id = data.get("loan_id")

    if loan_id is None:
        return {
            "success": False,
            "message": "loan_id is required."
        }, 400

    return predict_loan_application(loan_id)


@prediction_bp.route("/prediction/<int:prediction_id>", methods=["GET"])
@jwt_required()
def fetch_prediction(prediction_id):
    """
    Get Prediction By ID
    ---
    tags:
      - Prediction
    security:
      - Bearer: []
    parameters:
      - in: path
        name: prediction_id
        type: integer
        required: true
    responses:
      200:
        description: Prediction details
      404:
        description: Prediction not found
    """
    return get_prediction(prediction_id)


@prediction_bp.route("/predictions", methods=["GET"])
@jwt_required()
def fetch_all_predictions():
    """
    Get All Predictions
    ---
    tags:
      - Prediction
    security:
      - Bearer: []
    parameters:
      - in: query
        name: page
        type: integer
      - in: query
        name: size
        type: integer
      - in: query
        name: search
        type: string
      - in: query
        name: sortBy
        type: string
      - in: query
        name: order
        type: string
    responses:
      200:
        description: Prediction list
    """

    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 5, type=int)
    search = request.args.get("search", "", type=str)
    sort_by = request.args.get("sortBy", "prediction_id", type=str)
    order = request.args.get("order", "asc", type=str)

    return get_all_predictions(
        page,
        size,
        search,
        sort_by,
        order
    )


@prediction_bp.route("/prediction/<int:prediction_id>", methods=["DELETE"])
@jwt_required()
def remove_prediction(prediction_id):
    """
    Delete Prediction
    ---
    tags:
      - Prediction
    security:
      - Bearer: []
    parameters:
      - in: path
        name: prediction_id
        type: integer
        required: true
    responses:
      200:
        description: Prediction deleted successfully
      404:
        description: Prediction not found
    """
    return delete_prediction(prediction_id)