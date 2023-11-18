import requests

class ApiRequest:
    

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def make_get_request(self):
        response = requests.get(self.url, headers=self.headers)
        return response

    def get_status_code(self):
        return response.status_code






