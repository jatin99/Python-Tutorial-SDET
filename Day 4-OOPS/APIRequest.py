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





# Example usage
url = "http://139.59.91.96:9000/v1/userdetails"
headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZmlyc3RfbmFtZSI6ImZkIiwibGFzdF9uYW1lIjoiZmQiLCJsb2dpbl9pZCI6ImlhbWZkIiwibW9iaWxlX251bWJlciI6Ijg4OTk3NzY2NTUiLCJlbWFpbF9pZCI6Im1hcmtAZ21haWwuY29tIiwicGFzc3dvcmQiOiI1ZjRkY2MzYjVhYTc2NWQ2MWQ4MzI3ZGViODgyY2Y5OSIsInJlc2V0X3Bhc3N3b3JkX2RhdGUiOm51bGwsImxvY2tfc3RhdHVzIjowLCJpc19hY3RpdmUiOjEsIm1zdF9yb2xlX2lkIjo1LCJtc3Rfc2VydmljZV9sb2NhdGlvbl9pZCI6MSwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDNUMDg6MDY6MjMuMDAwWiIsIm1vZGlmaWVkX2F0IjoiMjAyMS0xMS0wM1QwODowNjoyMy4wMDBaIiwicm9sZV9uYW1lIjoiRnJvbnREZXNrIiwic2VydmljZV9sb2NhdGlvbiI6IlNlcnZpY2UgQ2VudGVyIEEiLCJpYXQiOjE2OTk2ODUyOTd9.ozabiqqD2sNCIOPr9kHzg5JIeo8QyZEFmCzx3RAEWYA"
}

api_client = ApiRequest(url, headers)
response = api_client.make_get_request()
print("Response Body", response.json().get("data").get("id"))
print("Status Code:", api_client.get_status_code())
