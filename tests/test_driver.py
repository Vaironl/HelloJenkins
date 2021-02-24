from flask import app
import pytest

def setUp():
    app.testing = True
    self.app = app.test_client()

def test_hello_with_name(self):
    name = "John"
    rv = self.app.get('/hello/John')
    assert rv.status == '200 OK'
    assert rv.data == b'<h1>Hello John!</h1>\n'
        
# if __name__ == '__main__':
