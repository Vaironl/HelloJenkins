import flask
import pytest
from pathlib import Path
from app.driver import app

@pytest.fixture
def setUp():
    yield app.test_client()

def test_index(client):
    return app.