"""" HTTP GET Requests With Query Params """
import requests

url = 'http://something.com'
params = {
    'param_1': 'value_1',
    'param_2': 'value_2',
}

response = requests.get(url, params)

# Show response with JSON body
print(response.json())
