from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from extensions import db
from models.user import User
from utils.logger import logger


def register_user(data):

    existing_user = User.query.filter_by(email=data["email"]).first()

    if existing_user:
        logger.warning(
            f"Registration failed. Email already exists: {data['email']}"
        )
        return {
            "success": False,
            "message": "Email already registered."
        }, 409

    user = User(
        name=data["name"],
        email=data["email"],
        password=generate_password_hash(data["password"]),
        role=data.get("role", "USER").upper()
    )

    db.session.add(user)
    db.session.commit()

    logger.info(f"New user registered: {user.email}")

    return {
        "success": True,
        "message": "User registered successfully."
    }, 201


def login_user(data):

    email = data.get("email", "").strip()
    password = data.get("password", "")

    user = User.query.filter_by(email=email).first()

    if user is None:
        logger.warning(f"Login failed. User not found: {email}")
        return {
            "success": False,
            "message": "Invalid email or password."
        }, 401

    if not check_password_hash(user.password, password):
        logger.warning(
            f"Login failed. Incorrect password for: {email}"
        )
        return {
            "success": False,
            "message": "Invalid email or password."
        }, 401

    access_token = create_access_token(
        identity=str(user.user_id),
        additional_claims={
            "role": user.role
        }
    )

    logger.info(f"User logged in: {user.email}")

    return {
        "success": True,
        "message": "Login successful.",
        "access_token": access_token,
        "user": {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }, 200


def get_profile(user_id):

    user = db.session.get(User, user_id)

    if user is None:
        logger.warning(
            f"Profile not found. User ID: {user_id}"
        )
        return {
            "success": False,
            "message": "User not found."
        }, 404

    logger.info(f"Profile viewed. User: {user.email}")

    return {
        "success": True,
        "data": {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "created_at": user.created_at
        }
    }, 200


def change_password(user_id, data):

    user = db.session.get(User, user_id)

    if user is None:
        logger.warning(
            f"Password change failed. User ID {user_id} not found."
        )
        return {
            "success": False,
            "message": "User not found."
        }, 404

    old_password = data.get("old_password")
    new_password = data.get("new_password")

    if not old_password or not new_password:
        logger.warning(
            f"Password change failed. Missing password fields for {user.email}"
        )
        return {
            "success": False,
            "message": "Old password and new password are required."
        }, 400

    if not check_password_hash(user.password, old_password):
        logger.warning(
            f"Password change failed. Incorrect old password for {user.email}"
        )
        return {
            "success": False,
            "message": "Old password is incorrect."
        }, 400

    user.password = generate_password_hash(new_password)

    db.session.commit()

    logger.info(f"Password changed: {user.email}")

    return {
        "success": True,
        "message": "Password changed successfully."
    }, 200