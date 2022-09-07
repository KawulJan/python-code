import json

import jsonpath
import requests

#API URL
url ="https://reqres.in/api/users?page=2"

#read input json file
file=open("C:\\Users\\aytol\\OneDrive\\Desktop\\CreatJison001.json", 'r')
json_input =file.read()
request_json = json.loads(json_input)

#make put request with json input bady
response =requests.put(url,request_json)
#print(response.content)

    #willing response code
assert  response.status_code==200


#parse responsecontent
response_json =json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json,'updatedAt')
print(updated_li[0])
