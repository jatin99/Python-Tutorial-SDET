import requests

class APIRequest:
    BASE_URL = "http://139.59.91.96:9000/v1/"

    def __init__(self):
        self.response = None

    def get(self, endpoint):
        self.response = requests.get(APIRequest.BASE_URL + endpoint)
        return self

    def post(self, endpoint, data=None, headers=None):
        self.response = requests.post(APIRequest.BASE_URL + endpoint, json=data, headers=headers)
        return self

    def put(self, endpoint, data=None, headers=None):
        self.response = requests.put(APIRequest.BASE_URL + endpoint, json=data, headers=headers)
        return self

    def delete(self, endpoint, headers=None):
        self.response = requests.delete(APIRequest.BASE_URL + endpoint, headers=headers)
        return self

    def with_headers(self, headers):
        # Clone the instance and set new headers
        new_instance = self._clone()
        new_instance.response = None  # Reset the response for a new request
        new_instance.headers = headers
        return new_instance

    def with_params(self, params):
        # Clone the instance and set new parameters
        new_instance = self._clone()
        new_instance.response = None  # Reset the response for a new request
        new_instance.params = params
        return new_instance

    def status_code(self):
        return self.response.status_code

    def json_body(self):
        return self.response.json() if 'application/json' in self.response.headers.get('content-type', '') else None

    def _clone(self):
        # Helper method to clone the instance
        new_instance = APIRequest()
        new_instance.response = self.response
        return new_instance

# Example usage:
headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZmlyc3RfbmFtZSI6ImZkIiwibGFzdF9uYW1lIjoiZmQiLCJsb2dpbl9pZCI6ImlhbWZkIiwibW9iaWxlX251bWJlciI6Ijg4OTk3NzY2NTUiLCJlbWFpbF9pZCI6Im1hcmtAZ21haWwuY29tIiwicGFzc3dvcmQiOiI1ZjRkY2MzYjVhYTc2NWQ2MWQ4MzI3ZGViODgyY2Y5OSIsInJlc2V0X3Bhc3N3b3JkX2RhdGUiOm51bGwsImxvY2tfc3RhdHVzIjowLCJpc19hY3RpdmUiOjEsIm1zdF9yb2xlX2lkIjo1LCJtc3Rfc2VydmljZV9sb2NhdGlvbl9pZCI6MSwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDNUMDg6MDY6MjMuMDAwWiIsIm1vZGlmaWVkX2F0IjoiMjAyMS0xMS0wM1QwODowNjoyMy4wMDBaIiwicm9sZV9uYW1lIjoiRnJvbnREZXNrIiwic2VydmljZV9sb2NhdGlvbiI6IlNlcnZpY2UgQ2VudGVyIEEiLCJpYXQiOjE2OTk2ODUyOTd9.ozabiqqD2sNCIOPr9kHzg5JIeo8QyZEFmCzx3RAEWYA"   
}

params = {
    "param1": "value1",
    "param2": "value2"
}

statusCode = (
    APIRequest()
        .get("userdetails")
        .with_headers(headers)
        .status_code()
)

print("Status Code:", statusCode)
