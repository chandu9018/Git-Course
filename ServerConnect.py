import requests;
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.status_code)
print(response.json())
print(response.json()['userId'])
print(response.json()['title'])
print(response.json()['completed'])