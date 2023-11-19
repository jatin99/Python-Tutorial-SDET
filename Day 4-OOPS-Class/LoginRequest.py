import requests
#BASE_URL IS CONSTANT
BASE_URL = "http://139.59.91.96:9000/v1/"

def make_get_request(url, headers):

    response = requests.get(url,headers= headers)  #GET API REQUEST
    return response


def make_post_request(url, data, headers):
    response = requests.post(url, data = data ,headers= headers)  #POST API REQUEST
    return response

#USER_DETAILS API REQUEST
headers = {
    
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZmlyc3RfbmFtZSI6ImZkIiwibGFzdF9uYW1lIjoiZmQiLCJsb2dpbl9pZCI6ImlhbWZkIiwibW9iaWxlX251bWJlciI6Ijg4OTk3NzY2NTUiLCJlbWFpbF9pZCI6Im1hcmtAZ21haWwuY29tIiwicGFzc3dvcmQiOiI1ZjRkY2MzYjVhYTc2NWQ2MWQ4MzI3ZGViODgyY2Y5OSIsInJlc2V0X3Bhc3N3b3JkX2RhdGUiOm51bGwsImxvY2tfc3RhdHVzIjowLCJpc19hY3RpdmUiOjEsIm1zdF9yb2xlX2lkIjo1LCJtc3Rfc2VydmljZV9sb2NhdGlvbl9pZCI6MSwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDNUMDg6MDY6MjMuMDAwWiIsIm1vZGlmaWVkX2F0IjoiMjAyMS0xMS0wM1QwODowNjoyMy4wMDBaIiwicm9sZV9uYW1lIjoiRnJvbnREZXNrIiwic2VydmljZV9sb2NhdGlvbiI6IlNlcnZpY2UgQ2VudGVyIEEiLCJpYXQiOjE2OTk2ODUyOTd9.ozabiqqD2sNCIOPr9kHzg5JIeo8QyZEFmCzx3RAEWYA"   
} 



#LOGIN API REQUEST


login_data = {
    "username": "iamfd",
    "password": "password"
    
}


login_headers = {
    "Content-Type" : "application/json"
    
} 
r =make_post_request(BASE_URL+"login", login_data,login_headers)
print(r.status_code)