def test_create_applicant(client, access_token):

    response = client.post(
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

    assert response.status_code == 201

    data = response.get_json()

    assert data["success"] is True
    assert "applicant_id" in data
def test_get_applicant(client, access_token):

    create = client.post(
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

    applicant_id = create.get_json()["applicant_id"]

    response = client.get(
        f"/applicant/{applicant_id}",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True

def test_get_all_applicants(client, access_token):

    response = client.get(
        "/applicants",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True
def test_update_applicant(client, access_token):

    create = client.post(
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

    applicant_id = create.get_json()["applicant_id"]

    response = client.put(
        f"/applicant/{applicant_id}",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "gender": "Female",
            "married": "No",
            "dependents": "2",
            "education": "Graduate",
            "self_employed": "Yes",
            "property_area": "Rural"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True
def test_patch_applicant(client, access_token):

    create = client.post(
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

    applicant_id = create.get_json()["applicant_id"]

    response = client.patch(
        f"/applicant/{applicant_id}",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "property_area": "Semiurban"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True
def test_delete_applicant(client, access_token):

    create = client.post(
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

    applicant_id = create.get_json()["applicant_id"]

    response = client.delete(
        f"/applicant/{applicant_id}",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True