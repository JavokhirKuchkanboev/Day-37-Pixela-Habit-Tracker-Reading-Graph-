import requests
import os
from datetime import datetime

today = datetime.now().strftime("%Y%m%d")

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")

if not TOKEN or not USERNAME:
    raise ValueError("Environment variables not set")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_id = "graph01"
graph_config = {
    "id": graph_id,
    "name": "Reading Graph",
    "unit": "page",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

posting_endpoint = f"{graph_endpoint}/{graph_id}"

posting_config = {
    "date": today,
    "quantity": "25",
}

response = requests.post(url=posting_endpoint, json=posting_config, headers=headers)
print(response.text)