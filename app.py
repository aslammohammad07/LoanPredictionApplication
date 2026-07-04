from flask import Flask
from flasgger import Swagger

from config import Config
from extensions import db, jwt, cors
from handlers.exception_handler import register_error_handlers
from routes.auth_routes import auth_bp
from routes.applicant_routes import applicant_bp
from routes.loan_routes import loan_bp
from routes.prediction_routes import prediction_bp
from routes.dashboard_routes import dashboard_bp

from utils.token_blocklist import BLOCKLIST

app = Flask(__name__)

app.config.from_object(Config)

swagger = Swagger(app)

print("DATABASE URI:", app.config.get("SQLALCHEMY_DATABASE_URI"))

db.init_app(app)
jwt.init_app(app)
cors.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(applicant_bp)
app.register_blueprint(loan_bp)
app.register_blueprint(prediction_bp)
app.register_blueprint(dashboard_bp)

register_error_handlers(app)


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST


@app.route("/")
def home():
    return {
        "application": "LoanPredictionApplication",
        "version": "1.0",
        "status": "Running Successfully"
    }


@app.route("/test")
def test():
    return "Working"


if __name__ == "__main__":

    print("\n========== Registered Routes ==========")
    for rule in app.url_map.iter_rules():
        print(rule)
    print("=======================================\n")

    app.run(debug=True)