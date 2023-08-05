import requests
import json

url = "https://api.midjourneyapi.io/v2/imagine"
def generate(prmpt):
    headers = {
        "Authorization": "API_key",  # Replace 'API_key' with your actual API key
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prmpt
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    # printing the output
    return response.text
