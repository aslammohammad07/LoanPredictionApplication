from models.user import User
from models.applicant import Applicant
from models.loan import LoanApplication
from models.prediction import Prediction

from utils.logger import logger


def get_dashboard():

    total_users = User.query.count()
    total_applicants = Applicant.query.count()
    total_loans = LoanApplication.query.count()
    total_predictions = Prediction.query.count()

    approved = Prediction.query.filter_by(
        prediction="Approved"
    ).count()

    rejected = Prediction.query.filter_by(
        prediction="Rejected"
    ).count()

    approval_rate = 0

    if total_predictions > 0:
        approval_rate = round(
            (approved / total_predictions) * 100,
            2
        )

    rejection_rate = 0

    if total_predictions > 0:
        rejection_rate = round(
            (rejected / total_predictions) * 100,
            2
        )

    logger.info(
        f"Dashboard accessed | Users: {total_users}, "
        f"Applicants: {total_applicants}, "
        f"Loans: {total_loans}, "
        f"Predictions: {total_predictions}, "
        f"Approved: {approved}, "
        f"Rejected: {rejected}"
    )

    return {
        "success": True,
        "dashboard": {
            "total_users": total_users,
            "total_applicants": total_applicants,
            "total_loans": total_loans,
            "total_predictions": total_predictions,
            "approved_loans": approved,
            "rejected_loans": rejected,
            "approval_rate": approval_rate,
            "rejection_rate": rejection_rate
        }
    }, 200