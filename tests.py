from fastapi.testclient import TestClient

from src.api.ping.base import router_ping_db

client = TestClient(router_ping_db)


def test_ping():
    response = client.get('/')
    assert response.status_code == 201

