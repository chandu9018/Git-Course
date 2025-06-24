import requests;
from UrlApi import api
from UserDetails import UserName
from UserDetails import PassWord
response = requests.get(api)
print(response.status_code)
print(response.json())
print(response.json()['userId'])
print(response.json()['title'])
print(response.json()['completed'])
print(UserName)
print(PassWord)
#Python rest api call to  External System to Get Json Response Object Beta Version