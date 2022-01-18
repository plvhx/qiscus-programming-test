import json
import requests

import service.client_method as m


class Client(object):
    def __init__(self, base_url=""):
        self.headers = {}
        self.base_url = base_url

    def get_headers(self):
        return self.headers

    def set_headers(self, headers):
        self.headers = headers
        return self

    def add_header(self, key, value):
        self.headers[key] = value
        return self

    def get_header(self, key):
        try:
            self.headers[key]
        except KeyError as e:
            return None

        return self.headers[key]

    def get_base_url(self):
        return self.base_url

    def set_base_url(self, base_url):
        self.base_url = base_url
        return self

    def is_json(self, headers):
        return True if headers["Content-Type"] == "application/json" else False

    def dispatch(self, method, url, data=None):
        try:
            if method == m.GET:
                r = requests.get(url, headers=self.get_headers())
            elif method == m.POST:
                r = requests.post(url, headers=self.get_headers(), data=data)
            elif method == m.PUT:
                r = requests.put(url, headers=self.get_headers(), data=data)
            elif method == m.PATCH:
                r = requests.patch(url, headers=self.get_headers(), data=data)
            elif method == m.DELETE:
                r = requests.delete(url, headers=self.get_headers())
        except Exception as e:
            return None

        if not self.is_json(r.headers):
            return None

        return r.json()

    def get(self, url, data=None):
        return self.dispatch(m.GET, url, data)

    def post(self, url, data=None):
        return self.dispatch(m.POST, url, data)

    def put(self, url, data=None):
        return self.dispatch(m.PUT, url, data)

    def patch(self, url, data=None):
        return self.dispatch(m.PATCH, url, data)

    def delete(self, url, data=None):
        return self.dispatch(m.DELETE, url, data)
