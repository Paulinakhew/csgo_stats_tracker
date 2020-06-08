import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()
API_KEY = os.environ.get("API_KEY")
headers = {'TRN-Api-Key': API_KEY}

app = Flask(__name__)


@app.route('/', methods=['GET'])
def dashboard():
    data = requests.get("https://public-api.tracker.gg/v2/csgo/standard/profile/steam/76561199056418213", headers=headers).json()
    return render_template('dashboard.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
