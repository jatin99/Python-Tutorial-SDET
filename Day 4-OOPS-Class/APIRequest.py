import requests

class APIRequest:
    BASE_URL = "http://139.59.91.96:9000/v1/"

    def __init__(self):
        self.response = None
        self.x =10

    def get_request(self, headers, endpoint):
        self.response = requests.get(APIRequest.BASE_URL + endpoint, headers=headers)
        return self  # Return the instance to allow chaining

    def get_statuscode(self):
        return self.response.status_code
    
    def get_json_body(self):
        return self.response.json()

headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZmlyc3RfbmFtZSI6ImZkIiwibGFzdF9uYW1lIjoiZmQiLCJsb2dpbl9pZCI6ImlhbWZkIiwibW9iaWxlX251bWJlciI6Ijg4OTk3NzY2NTUiLCJlbWFpbF9pZCI6Im1hcmtAZ21haWwuY29tIiwicGFzc3dvcmQiOiI1ZjRkY2MzYjVhYTc2NWQ2MWQ4MzI3ZGViODgyY2Y5OSIsInJlc2V0X3Bhc3N3b3JkX2RhdGUiOm51bGwsImxvY2tfc3RhdHVzIjowLCJpc19hY3RpdmUiOjEsIm1zdF9yb2xlX2lkIjo1LCJtc3Rfc2VydmljZV9sb2NhdGlvbl9pZCI6MSwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDNUMDg6MDY6MjMuMDAwWiIsIm1vZGlmaWVkX2F0IjoiMjAyMS0xMS0wM1QwODowNjoyMy4wMDBaIiwicm9sZV9uYW1lIjoiRnJvbnREZXNrIiwic2VydmljZV9sb2NhdGlvbiI6IlNlcnZpY2UgQ2VudGVyIEEiLCJpYXQiOjE2OTk2ODUyOTd9.ozabiqqD2sNCIOPr9kHzg5JIeo8QyZEFmCzx3RAEWYA"   
}



print("Status Code:", APIRequest().get_request(headers, "userdetails").get_json_body())
