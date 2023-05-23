from app import app
import pytest


@pytest.fixture()
def app_test_client():
    return app.test_client()


def test_form_input(app_test_client):
    assert app_test_client.get("/").status_code == 200
