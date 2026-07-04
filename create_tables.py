from app import app
from extensions import db

from models.user import User
from models.applicant import Applicant
from models.loan import LoanApplication
from models.prediction import Prediction
from models.model_details import ModelDetails

with app.app_context():
    db.create_all()
    print("All tables created successfully!")