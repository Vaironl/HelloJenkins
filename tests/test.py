import pytest
import flask

class test_simple_app(app):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    
#     def test_hello_with_name(self):
#         name = "John"
#         rv = self.app.get('/hello/John')
#         self.assertEqual(rv.status, '200 OK')
#         self.assertEqual(rv.data, b'<h1>Hello John!</h1>\n')
        

# if __name__ == '__main__':
