import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, redirect
import models as m


load_dotenv()
API_KEY = os.environ.get("API_KEY")
headers = {'TRN-Api-Key': API_KEY}

app = Flask(__name__)


@app.route('/', methods=['GET'])
def dashboard():
    resp = requests.get(
        url="https://public-api.tracker.gg/v2/csgo/standard/profile/steam/76561199056418213",
        headers=headers
    )

    data = resp.json()['data']

    return_dict = m.process_json_data(data=data)

    return render_template('dashboard.html', data=return_dict)


@app.route('/<steam_id>')
def user_dashboard(steam_id):
    resp = requests.get(
        url=f"https://public-api.tracker.gg/v2/csgo/standard/profile/steam/{steam_id}",
        headers=headers
    )
    print(f"https://public-api.tracker.gg/v2/csgo/standard/profile/steam/{steam_id}")
    if resp.status_code == 200:
        data = resp.json()['data']

        return_dict = m.process_json_data(data=data)

        return render_template('dashboard.html', data=return_dict)
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
