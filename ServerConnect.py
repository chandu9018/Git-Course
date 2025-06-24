import requests;
from UserDetails import api
response = requests.get(api)
print(response.status_code)
print(response.json())
print(response.json()['userId'])
print(response.json()['title'])
print(response.json()['completed'])
#Python rest api call to  External System to Get Json Response Object Beta Version