import requests
import json

def get_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        print("Error: Unable to retrieve data from API")
        return None

def print_data(data):
    if data:
        print("Data:")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("No data to display")

api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"

data = get_data_from_api(api_url)
print_data(data)