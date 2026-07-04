from config import Config


class TestConfig(Config):

    TESTING = True

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:root@localhost:3306/LoanPredictionTestDB"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False