import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, json={"query": "Hello world"})
print(get_response.text)
print(get_response.status_code)


# HTTP Request -> HTML
# REST API HTTP REQUEST -> JSON
# JAVASCRIPT Object Notation ~ Python Dict
print(get_response.json())
# print(get_response.status_code)
