from MyAPIUtil import APIUtil


headers = {
 
    }


payload = {
    "username": "iamfd",
    "password": "password"
    
}

def test_login_api_request():
        response =APIUtil.make_post_request("login",payload,headers )
        print(response.status_code)
        print(response.json())


test_login_api_request()