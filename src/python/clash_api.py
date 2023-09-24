import requests
import os
CLAN_TAG = "%239RJOYLR9"
# Define the headers with the API token.
headers = {
    "Authorization": f"Bearer {os.environ.get('API_TOKEN_1')}"
}
def get_clan():
    API_URL = f"https://api.clashofclans.com/v1/clans/{CLAN_TAG}"
    try:
        # Make an HTTP GET request to the Clash of Clans API.
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            clan_data = response.json()
            return clan_data
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

def get_members():
    API_URL = f"https://api.clashofclans.com/v1/clans/{CLAN_TAG}/members"
    try:
        # Make an HTTP GET request to the Clash of Clans API.
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            clan_data = response.json()
            return clan_data
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

def get_member(data):
    API_URL = f"https://api.clashofclans.com/v1/players/{data}"
    try:
        # Make an HTTP GET request to the Clash of Clans API.
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            clan_data = response.json()
            return clan_data
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
def get_war_history():
    API_URL = f"https://api.clashofclans.com/v1/clans/{CLAN_TAG}/warlog"
    try:
        # Make an HTTP GET request to the Clash of Clans API.
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            clan_data = response.json()
            return clan_data
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
