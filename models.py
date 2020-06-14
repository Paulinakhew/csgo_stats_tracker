import os
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.environ.get("API_KEY")
headers = {'TRN-Api-Key': API_KEY}


def process_json_data(data):
    platforminfo = data['platformInfo']
    stats = data['segments'][0]['stats']
    print(stats['wlPercentage']['value'])

    return_dict = {
        'avatar_url': platforminfo['avatarUrl'],
        'username': platforminfo['platformUserHandle'],
        'time_played': stats['timePlayed']['displayValue'],
        'kills': stats['kills']['value'],
        'deaths': stats['deaths']['value'],
        'kd': round(stats['kd']['value'], 2),
        'kd_total': round(stats['kd']['value'], 2) + 1.00,
        'kd_fraction': round(stats['kd']['value'] / (stats['kd']['value'] + 1.00), 2) * 100,
        'wins': stats['wins']['value'],
        'losses': stats['losses']['value'],
        'headshots': stats['headshots']['value'],
        'headshotpct': stats['headshotPct']['value'],
        'headshot_percentile': stats['headshotPct']['percentile'],
        'kd_percentile': stats['kd']['percentile'],
        'wl_percentage': stats['wlPercentage']['value'],
        'wl_percentile': stats['wlPercentage']['percentile']
    }

    return return_dict


def request_tracker_network_api(steam_id=76561199056418213):
    resp = requests.get(
        url=f"https://public-api.tracker.gg/v2/csgo/standard/profile/steam/{steam_id}",
        headers=headers
    )

    return resp
