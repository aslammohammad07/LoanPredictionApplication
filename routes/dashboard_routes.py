from flask import Blueprint
from flask_jwt_extended import jwt_required

from services.dashboard_service import get_dashboard
from utils.admin_required import admin_required

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard", methods=["GET"])
@jwt_required()
@admin_required()
def dashboard():
    """
    Dashboard Statistics
    ---
    tags:
      - Dashboard
    security:
      - Bearer: []
    responses:
      200:
        description: Dashboard statistics
      403:
        description: Admin access required
      401:
        description: Unauthorized
    """

    return get_dashboard()