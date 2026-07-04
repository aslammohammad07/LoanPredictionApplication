import uuid


def test_home(client):

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "LoanPredictionApplication"


def test_register(client):

    email = f"test_{uuid.uuid4().hex[:8]}@gmail.com"

    response = client.post(
        "/register",
        json={
            "name": "Test User",
            "email": email,
            "password": "123456"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["success"] is True


def test_login(client):

    email = f"test_{uuid.uuid4().hex[:8]}@gmail.com"

    register = client.post(
        "/register",
        json={
            "name": "Test User",
            "email": email,
            "password": "123456"
        }
    )

    assert register.status_code == 201

    response = client.post(
        "/login",
        json={
            "email": email,
            "password": "123456"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True
    assert "access_token" in data


def test_profile(client, access_token):

    response = client.get(
        "/profile",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True


def test_change_password(client, access_token):

    response = client.patch(
        "/change-password",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "old_password": "123456",
            "new_password": "12345678"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True


def test_logout(client, access_token):

    response = client.post(
        "/logout",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True