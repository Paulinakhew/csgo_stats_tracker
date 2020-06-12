import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template
import models as m


load_dotenv()
API_KEY = os.environ.get("API_KEY")
headers = {'TRN-Api-Key': API_KEY}

app = Flask(__name__)


@app.route('/', methods=['GET'])
def dashboard():
    data = requests.get(
        url="https://public-api.tracker.gg/v2/csgo/standard/profile/steam/76561199056418213",
        headers=headers
    ).json()['data']

    return_dict = m.process_json_data(data=data)

    return render_template('dashboard.html', data=return_dict)


if __name__ == '__main__':
    app.run(debug=True)
