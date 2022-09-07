import json

import jsonpath
import requests

#API URL
url ="https://reqres.in/api/users"

def test_create_new_user():
    # read input json file
    file = open("C:\\Users\\aytol\\OneDrive\\Desktop\\CreatJison001.json", 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    # make post request with json input bady
    response = requests.post(url, request_json)
    # print(response.content)
    # willing response code
    assert response.status_code == 201
    # fetch header from response
    print(response.headers)
    print(response.headers.get("Content-length"))
    # parse response to json farmat
    response_json = json.loads(response.text)
    # pick id using json path
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])
