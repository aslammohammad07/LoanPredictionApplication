import os
import sys
import uuid
import pytest

from werkzeug.security import generate_password_hash

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
from extensions import db
from models.user import User


@pytest.fixture
def client():

    app.config["TESTING"] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


@pytest.fixture
def access_token(client):

    email = f"test_{uuid.uuid4().hex[:8]}@gmail.com"

    client.post(
        "/register",
        json={
            "name": "Test User",
            "email": email,
            "password": "123456"
        }
    )

    login = client.post(
        "/login",
        json={
            "email": email,
            "password": "123456"
        }
    )

    data = login.get_json()

    assert login.status_code == 200

    return data["access_token"]


@pytest.fixture
def admin_access_token(client):

    email = f"admin_{uuid.uuid4().hex[:8]}@gmail.com"

    admin = User(
        name="Admin User",
        email=email,
        password=generate_password_hash("123456"),
        role="ADMIN"
    )

    db.session.add(admin)
    db.session.commit()

    login = client.post(
        "/login",
        json={
            "email": email,
            "password": "123456"
        }
    )

    assert login.status_code == 200

    data = login.get_json()

    return data["access_token"]