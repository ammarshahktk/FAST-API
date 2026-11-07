from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Test home api
def test_home():
    response = client.get("/")
    # Check Status Code
    assert response.status_code == 200
    # Check Response Data 
    assert response.json() == {"message" : "Hello Ammar"}


# Testing Add API:
def test_add():
    response = client.get("/add?a=5&b=3")

    assert response.status_code == 200
    assert response.json() == {"result": 8}