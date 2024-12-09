import json
import requests
import math

# Replace with your actual API key and spreadsheet ID
# global api_key
secrets = []
with open("secrets.txt") as file:
    for line in file:
        secrets.append(line)

api_key = str(secrets[0]).strip()
spreadsheet_id = str(secrets[1]).strip()

url = "https://api.sheetson.com/v2/sheets/Sheet1/"


### FORMATTING NOTES FOR TILES
# EAST WEST NORTH SOUTH
# - East West North South

# returns a dictionary
def get(line: int):
    a = url + str(line)
    # Set up the query parameters
    params = {
        'apiKey': api_key,
        'spreadsheetId': spreadsheet_id
    }

    # Make the GET request
    response = requests.get(a, params=params)

    # Check the response status and print the result
    if response.status_code == 200:
        print(response.json())  # Print the JSON response
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")

# returns a dictionary
def set(pos: str, data: str, line: int):
    a = url + str(line)
    # Set up the headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "X-Spreadsheet-Id": spreadsheet_id,
        "Content-Type": "application/json"
    }

    # Set up the data to be sent in the PUT request
    data = {
        pos: data
    }

    # Make the PUT request
    response = requests.put(a, headers=headers, data=json.dumps(data))

    # Check the response status and print the result
    if response.status_code == 200:
        print("Update successful:", response.json())  # Print the JSON response
        return response.json
    else:
        print(f"Error: {response.status_code} - {response.text}")

get(2)