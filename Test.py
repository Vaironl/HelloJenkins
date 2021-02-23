import unittest
from driver import app
class TestSimpleFlaskApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    
    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

if __name__ == '__main__':
    unittest.main()