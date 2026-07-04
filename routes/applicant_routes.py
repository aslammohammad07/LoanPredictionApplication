print("Applicant Routes Loaded")

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.applicant_service import (
    create_applicant,
    get_applicant,
    get_all_applicants,
    update_applicant,
    patch_applicant,
    delete_applicant
)

from schemas.applicant_schema import ApplicantSchema
from utils.validator import validate_request

applicant_bp = Blueprint("applicant", __name__)


@applicant_bp.route("/applicant", methods=["POST"])
@jwt_required()
def add_applicant():

    if not request.is_json:
        return {
            "success": False,
            "message": "Content-Type must be application/json"
        }, 415

    data, errors = validate_request(
        ApplicantSchema(),
        request.get_json()
    )

    if errors:
        return {
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }, 400

    user_id = int(get_jwt_identity())

    return create_applicant(data, user_id)


@applicant_bp.route("/applicant/<int:applicant_id>", methods=["GET"])
@jwt_required()
def fetch_applicant(applicant_id):

    return get_applicant(applicant_id)


@applicant_bp.route("/applicants", methods=["GET"])
@jwt_required()
def fetch_all_applicants():

    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 5, type=int)
    search = request.args.get("search", "", type=str)
    sort_by = request.args.get("sortBy", "applicant_id", type=str)
    order = request.args.get("order", "asc", type=str)

    return get_all_applicants(
        page,
        size,
        search,
        sort_by,
        order
    )


@applicant_bp.route("/applicant/<int:applicant_id>", methods=["PUT"])
@jwt_required()
def modify_applicant(applicant_id):

    if not request.is_json:
        return {
            "success": False,
            "message": "Content-Type must be application/json"
        }, 415

    data, errors = validate_request(
        ApplicantSchema(),
        request.get_json()
    )

    if errors:
        return {
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }, 400

    return update_applicant(applicant_id, data)


@applicant_bp.route("/applicant/<int:applicant_id>", methods=["PATCH"])
@jwt_required()
def modify_partial_applicant(applicant_id):

    if not request.is_json:
        return {
            "success": False,
            "message": "Content-Type must be application/json"
        }, 415

    data, errors = validate_request(
        ApplicantSchema(partial=True),
        request.get_json()
    )

    if errors:
        return {
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }, 400

    return patch_applicant(applicant_id, data)


@applicant_bp.route("/applicant/<int:applicant_id>", methods=["DELETE"])
@jwt_required()
def remove_applicant(applicant_id):

    return delete_applicant(applicant_id)