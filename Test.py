import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_strip(self):
        self.assertEqual("     foo     ".strip(), "foo")

if __name__ == '__main__':
    unittest.main()