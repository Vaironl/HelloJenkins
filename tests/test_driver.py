import pytest
from app import driver

@pytest.fixture
def client():
    driver.app.config['TESTING'] = True

    with driver.app.test_client() as client:
        yield client
