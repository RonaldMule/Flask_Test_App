import unittest
# import requests
import json
from flask_app import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()

    def test_dictionary_resp(self):
        response = self.app_tester.get('http://127.0.0.1:5000/inventory')
        print('response.status_code : ', response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_this(self):
        response = self.app_tester.get('http://127.0.0.1:5000/inventory')
        response_body = json.loads(response.data)
        self.assertFalse(response_body)


if __name__ == '__main__':
    unittest.main()






