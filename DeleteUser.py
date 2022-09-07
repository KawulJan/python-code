import requests

#API URL
url ="https://reqres.in/api/users?page=2 "

response =requests.delete(url)

#Fetch respons code
print(response.status_code)

assert response.status_code==204
