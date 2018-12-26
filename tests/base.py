import requests
import os


class TestRequest:
    base_url = os.environ.get('API_BASE_URL')
    headers = {
        'x-api-key': os.environ.get('API_KEY'),
        'Content-Type': 'application/x-protobuf',
    }

    def get(self, uri):
        return requests.get(
            self.base_url + uri,
            headers=self.headers
        )

    def post(self, uri, body):
        return requests.post(
            self.base_url + uri,
            body,
            headers=self.headers
        )

    def put(self, uri, body):
        return requests.put(
            self.base_url + uri,
            str(body).encode('utf-8'),
            headers=self.headers
        )

    def patch(self, uri, body):
        return requests.patch(
            self.base_url + uri,
            str(body).encode('utf-8'),
            headers=self.headers
        )
