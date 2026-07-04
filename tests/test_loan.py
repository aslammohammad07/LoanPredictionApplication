def test_create_loan(client, access_token):

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

    response = client.post(
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

    assert response.status_code == 201

    data = response.get_json()

    assert data["success"] is True
    assert "loan_id" in data


def test_get_loan(client, access_token):

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

    response = client.get(
        f"/loan/{loan_id}",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True


def test_get_all_loans(client, access_token):

    response = client.get(
        "/loans",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True


def test_update_loan(client, access_token):

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

    response = client.put(
        f"/loan/{loan_id}",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "applicant_id": applicant_id,
            "applicant_income": 8000,
            "coapplicant_income": 3000,
            "loan_amount": 200,
            "loan_term": 240,
            "credit_history": 1
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True


def test_patch_loan(client, access_token):

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

    response = client.patch(
        f"/loan/{loan_id}",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "loan_amount": 250
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True


def test_delete_loan(client, access_token):

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

    response = client.delete(
        f"/loan/{loan_id}",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True