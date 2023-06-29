""" Shows how to query metrics to a prometheus server
using promql and the python language.
"""
import requests

url = 'http://prometheus-server'
params = {
    'query': 'max(up) by (hostname)'
}

resp = requests.get(url, params)

print(resp.json())
