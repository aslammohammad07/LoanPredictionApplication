from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from services.auth_service import (
    register_user,
    login_user,
    get_profile,
    change_password
)

from utils.token_blocklist import BLOCKLIST

from schemas.auth_schema import (
    RegisterSchema,
    LoginSchema,
    ChangePasswordSchema
)

from utils.validator import validate_request

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    """
    Register User
    ---
    tags:
      - Authentication
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - email
            - password
          properties:
            name:
              type: string
              example: Mohammad Aslam
            email:
              type: string
              example: aslam@gmail.com
            password:
              type: string
              example: 123456
    responses:
      201:
        description: User registered successfully
      400:
        description: Validation failed
      409:
        description: Email already registered
    """

    if not request.is_json:
        return {
            "success": False,
            "message": "Content-Type must be application/json"
        }, 415

    data, errors = validate_request(
        RegisterSchema(),
        request.get_json()
    )

    if errors:
        return {
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }, 400

    return register_user(data)


@auth_bp.route("/login", methods=["POST"])
def login():
    """
    User Login
    ---
    tags:
      - Authentication
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              example: aslam@gmail.com
            password:
              type: string
              example: 123456
    responses:
      200:
        description: Login Successful
      400:
        description: Validation failed
      401:
        description: Invalid email or password
    """

    if not request.is_json:
        return {
            "success": False,
            "message": "Content-Type must be application/json"
        }, 415

    data, errors = validate_request(
        LoginSchema(),
        request.get_json()
    )

    if errors:
        return {
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }, 400

    return login_user(data)


@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    """
    Get User Profile
    ---
    tags:
      - Authentication
    security:
      - Bearer: []
    responses:
      200:
        description: User profile
      401:
        description: Unauthorized
    """

    return get_profile(int(get_jwt_identity()))


@auth_bp.route("/change-password", methods=["PATCH"])
@jwt_required()
def update_password():
    """
    Change Password
    ---
    tags:
      - Authentication
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
            - old_password
            - new_password
          properties:
            old_password:
              type: string
              example: 123456
            new_password:
              type: string
              example: 12345678
    responses:
      200:
        description: Password changed successfully
      400:
        description: Validation failed
      401:
        description: Unauthorized
    """

    if not request.is_json:
        return {
            "success": False,
            "message": "Content-Type must be application/json"
        }, 415

    data, errors = validate_request(
        ChangePasswordSchema(),
        request.get_json()
    )

    if errors:
        return {
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }, 400

    return change_password(
        int(get_jwt_identity()),
        data
    )


@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    """
    Logout User
    ---
    tags:
      - Authentication
    security:
      - Bearer: []
    responses:
      200:
        description: Logged out successfully
      401:
        description: Unauthorized
    """

    BLOCKLIST.add(get_jwt()["jti"])

    return {
        "success": True,
        "message": "Logged out successfully."
    }, 200