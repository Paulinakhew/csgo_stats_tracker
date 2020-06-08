import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("API_KEY")
headers = {'TRN-Api-Key': API_KEY}

print(requests.get("https://public-api.tracker.gg/v2/csgo/standard/profile/steam/76561199056418213", headers=headers).json())
