import flask
import pytest
from pathlib import Path
from app import driver

@pytest.fixture
def client():
    driver.app.config['TESTING'] = True

    with driver.app.test_client() as client:
        yield client
