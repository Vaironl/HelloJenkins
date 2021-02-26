from flask.testing import FlaskClient
import pytest
from app import driver

@pytest.fixture
def client():
    driver.app.config['TESTING'] = True

    with driver.app.test_client() as client:
        yield client

def test_index_page(client : FlaskClient):
    rv = client.get('/')
    assert b'Demo Flask Application' in rv.data
    assert b'Hello World' in rv.data

def tests_hello_page(client: FlaskClient):
    rv = client.get('/hello/')
    assert b'Hello Page' in rv.data
    assert b'Hello, World(s)!' in rv.data

def tests_hello_dir(client: FlaskClient):
    rv = client.get('/hello')
    assert b'Hello Page' in rv.data
    assert b'Hello, World(s)!' in rv.data

def tests_hello_page_with_name(client: FlaskClient):
    rv = client.get('/hello/Johnny')
    assert b'Hello Page' in rv.data
    assert b'Hello, Johnny!' in rv.data