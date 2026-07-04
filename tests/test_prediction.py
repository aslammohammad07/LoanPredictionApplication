def test_create_prediction(client, access_token):

    applicant = client.post(
        "/applicant",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "gender": "Male",
            "married": "Yes",
            "dependents": "1",
            "education": "Graduate",
            "self_employed": "No",
            "property_area": "Urban"
        }
    )

    applicant_id = applicant.get_json()["applicant_id"]

    loan = client.post(
        "/loan",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "applicant_id": applicant_id,
            "applicant_income": 5000,
            "coapplicant_income": 2000,
            "loan_amount": 150,
            "loan_term": 360,
            "credit_history": 1
        }
    )

    loan_id = loan.get_json()["loan_id"]

    response = client.post(
        "/predict",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "loan_id": loan_id
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True
    assert "prediction_id" in data


def test_get_prediction(client, access_token):

    applicant = client.post(
        "/applicant",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "gender": "Male",
            "married": "Yes",
            "dependents": "1",
            "education": "Graduate",
            "self_employed": "No",
            "property_area": "Urban"
        }
    )

    applicant_id = applicant.get_json()["applicant_id"]

    loan = client.post(
        "/loan",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "applicant_id": applicant_id,
            "applicant_income": 5000,
            "coapplicant_income": 2000,
            "loan_amount": 150,
            "loan_term": 360,
            "credit_history": 1
        }
    )

    loan_id = loan.get_json()["loan_id"]

    prediction = client.post(
        "/predict",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "loan_id": loan_id
        }
    )

    prediction_id = prediction.get_json()["prediction_id"]

    response = client.get(
        f"/prediction/{prediction_id}",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True


def test_get_all_predictions(client, access_token):

    applicant = client.post(
        "/applicant",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "gender": "Male",
            "married": "Yes",
            "dependents": "1",
            "education": "Graduate",
            "self_employed": "No",
            "property_area": "Urban"
        }
    )

    applicant_id = applicant.get_json()["applicant_id"]

    loan = client.post(
        "/loan",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "applicant_id": applicant_id,
            "applicant_income": 5000,
            "coapplicant_income": 2000,
            "loan_amount": 150,
            "loan_term": 360,
            "credit_history": 1
        }
    )

    loan_id = loan.get_json()["loan_id"]

    client.post(
        "/predict",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "loan_id": loan_id
        }
    )

    response = client.get(
        "/predictions",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True


def test_delete_prediction(client, access_token):

    applicant = client.post(
        "/applicant",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "gender": "Male",
            "married": "Yes",
            "dependents": "1",
            "education": "Graduate",
            "self_employed": "No",
            "property_area": "Urban"
        }
    )

    applicant_id = applicant.get_json()["applicant_id"]

    loan = client.post(
        "/loan",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "applicant_id": applicant_id,
            "applicant_income": 5000,
            "coapplicant_income": 2000,
            "loan_amount": 150,
            "loan_term": 360,
            "credit_history": 1
        }
    )

    loan_id = loan.get_json()["loan_id"]

    prediction = client.post(
        "/predict",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "loan_id": loan_id
        }
    )

    prediction_id = prediction.get_json()["prediction_id"]

    response = client.delete(
        f"/prediction/{prediction_id}",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True