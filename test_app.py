import unittest
from app import app

class TestBasic(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.status_code = response.status_code
        assert self.status_code == 200

if __name__ == "__main__":
    unittest.main()