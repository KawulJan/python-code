from webbrowser import get

import jsonpath
import requests
import  json



      #API test
url ="https://reqres.in/api/users?page=2 "


     #Send get request
response = requests.get(url)

#print(response)
#display Request Content
#print(response.content)
#print(response.headers)

    #Parse response to json format

json_reponse =json.loads(response.text)
#print(json_reponse)

      #Fetch value using Json path
pages =jsonpath.jsonpath(json_reponse,'total_pages')
#print(pages[0])
assert pages[0] ==4