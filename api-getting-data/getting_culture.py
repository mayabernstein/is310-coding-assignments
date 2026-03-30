import json

import requests
import apikey
import os
import pyeuropeana.apis as apis

#--------------------------------
# Soccer API request
#--------------------------------
soccer_api_key = apikey.load("SOCCER_API_KEY")

headers = {
    'X-RapidAPI-Key': soccer_api_key,
    'X-RapidAPI-Host': 'v3.football.api-sports.io'
}

soccer_url = "https://v3.football.api-sports.io/leagues"

response = requests.get(soccer_url, headers=headers)

if response.status_code == 200:
    print("\nFull Soccer API response for the query:")
    print(response.json())
else:
    print("Error:", response.status_code, response.text)
#--------------------------------
# Europeana API request
#--------------------------------
europeana_api_key = apikey.load("EUROPEANA_API_KEY")
os.environ['EUROPEANA_API_KEY'] = europeana_api_key

response_europeana = apis.search(
    query="Spanish Football League",
    qf="TYPE:VIDEO",
    reusability="open AND permission",
    media=True,
    thumbnail=True,
    landingpage=True,
    rows=100
)
print("\nFull Europeana response for the query:")
print(response_europeana.get('items', [])[1:])

# Save the item data as a JSON file
europeana_items = response_europeana.get('items', [])[1:]
filename = "europeana_item_data.json"
with open(filename, "w", encoding="utf-8") as f:
    json.dump(europeana_items, f, indent=2, ensure_ascii=False)
print(f"\nEuropeana item data saved to {filename}")

