import json
from unittest import TestCase

from handler import hello


class HandlerTest(TestCase):
    def test_hello(self):
        body = json.dumps(
            {"message": "Go Serverless v1.0! Your function executed successfully!", "input": {}}
        )
        expected = {
            'statusCode': 200, 
            'body': body
        }
        actual = hello({}, {})
        self.assertEqual(expected, actual)
