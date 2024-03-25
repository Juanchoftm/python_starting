import requests
import json

api_data = requests.get('https://rbn3bwlfb1.execute-api.us-east-1.amazonaws.com/getData/Loans')

data = api_data.json()

data_ordenada = sorted(data, key=lambda x: x['effectiveApr'])

for item in data_ordenada:
    print(item)