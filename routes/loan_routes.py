from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from services.loan_service import (
    create_loan,
    get_loan,
    get_all_loans,
    update_loan,
    patch_loan,
    delete_loan
)

from schemas.loan_schema import LoanSchema
from utils.validator import validate_request

loan_bp = Blueprint("loan", __name__)


@loan_bp.route("/loan", methods=["POST"])
@jwt_required()
def add_loan():

    if not request.is_json:
        return {
            "success": False,
            "message": "Content-Type must be application/json"
        }, 415

    data, errors = validate_request(
        LoanSchema(),
        request.get_json()
    )

    if errors:
        return {
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }, 400

    return create_loan(data)


@loan_bp.route("/loan/<int:loan_id>", methods=["GET"])
@jwt_required()
def fetch_loan(loan_id):

    return get_loan(loan_id)


@loan_bp.route("/loans", methods=["GET"])
@jwt_required()
def fetch_all_loans():

    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 5, type=int)
    search = request.args.get("search", "", type=str)
    sort_by = request.args.get("sortBy", "loan_id", type=str)
    order = request.args.get("order", "asc", type=str)

    return get_all_loans(
        page,
        size,
        search,
        sort_by,
        order
    )


@loan_bp.route("/loan/<int:loan_id>", methods=["PUT"])
@jwt_required()
def modify_loan(loan_id):

    if not request.is_json:
        return {
            "success": False,
            "message": "Content-Type must be application/json"
        }, 415

    data, errors = validate_request(
        LoanSchema(),
        request.get_json()
    )

    if errors:
        return {
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }, 400

    return update_loan(loan_id, data)


@loan_bp.route("/loan/<int:loan_id>", methods=["PATCH"])
@jwt_required()
def modify_partial_loan(loan_id):

    if not request.is_json:
        return {
            "success": False,
            "message": "Content-Type must be application/json"
        }, 415

    data, errors = validate_request(
        LoanSchema(partial=True),
        request.get_json()
    )

    if errors:
        return {
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }, 400

    return patch_loan(loan_id, data)


@loan_bp.route("/loan/<int:loan_id>", methods=["DELETE"])
@jwt_required()
def remove_loan(loan_id):

    return delete_loan(loan_id)