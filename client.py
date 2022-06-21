import requests


endpoint = "http://127.0.0.1:8000/api/"
get_response = requests.get(endpoint,params={"Data":"Hello World!"})
# print(get_response.text)
print(get_response.json())