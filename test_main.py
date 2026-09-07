from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Test Home API
def test_home():
    response = client.get("/")

    # Status Code Check
    assert response.status_code == 200

    # Response Data Check
    assert response.json() == {"message": "hello world"}


# Test ADD API
def test_add():
    response = client.get("/add?a=5&b=3")

    assert response.status_code == 200
    assert response.json() == {"result": 8}
