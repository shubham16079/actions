import pytest
from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_index_returns_200(client):
    rv = client.get("/")
    assert rv.status_code == 200


def test_index_returns_hello_world(client):
    rv = client.get("/")
    assert b"Hello, World!" in rv.data
    assert b"github actions" in rv.data
