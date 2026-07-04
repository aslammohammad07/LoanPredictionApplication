def test_dashboard(client, admin_access_token):

    response = client.get(
        "/dashboard",
        headers={
            "Authorization": f"Bearer {admin_access_token}"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True

    assert "dashboard" in data

    assert "total_users" in data["dashboard"]
    assert "total_applicants" in data["dashboard"]
    assert "total_loans" in data["dashboard"]
    assert "total_predictions" in data["dashboard"]
    assert "approved_loans" in data["dashboard"]
    assert "rejected_loans" in data["dashboard"]
    assert "approval_rate" in data["dashboard"]
    assert "rejection_rate" in data["dashboard"]