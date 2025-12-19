import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

@pytest.fixture
def test_client():
    return client

# Test for getting activities
def test_get_activities(test_client):
    response = test_client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Test for signing up for an activity
def test_signup_activity(test_client):
    response = test_client.post("/activities/Chess Club/signup?email=test@mergington.edu")
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]

# Test for removing a participant
def test_remove_participant(test_client):
    response = test_client.delete("/activities/Chess Club/remove?email=test@mergington.edu")
    assert response.status_code == 200
    assert "Removed" in response.json()["message"]