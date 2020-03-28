import json
import os
import re
from unittest import TestCase, mock

from handler import url_generator
from processor import UrlProcessor


class UrlProcessorTest(TestCase):
    def setUp(self):
        os.environ['ROOT_URL'] = ''
        self.url_processor = UrlProcessor()

    def test_generate_url(self):
        url = self.url_processor.generate()
        r = re.match('\w+', url)
        self.assertEqual(r.string, url)
        self.assertEqual(len(url), 7)

    def test_generate_different_urls(self):
        url1 = self.url_processor.generate()
        url2 = self.url_processor.generate()
        url3 = self.url_processor.generate()
        url4 = self.url_processor.generate()
        all_generated_urls = {url1, url2, url3, url4}
        self.assertEqual(len(all_generated_urls), 4)


class UrlHandlerTest(TestCase):

    @mock.patch('processor.UrlProcessor.generate')
    def test_url_generator(self, mocked_url):
        url_string = '123asdf'
        mocked_url.return_value = url_string
        url = url_generator({}, {})
        expected = {
            'body': json.dumps({"newUrl": url_string}),
            'statusCode': 200,
            'headers': {}
        }
        self.assertEqual(url, expected)
