import os
import requests
from dotenv import load_dotenv


load_dotenv()
STEAM_WEB_API_KEY = os.environ.get("STEAM_WEB_API_KEY")


def process_json_data(data):
    stats = data['playerstats']['stats']
    kills = stats[0]['value']
    deaths = stats[1]['value']
    return_dict = {
        'avatar_url': None,
        'username': None,
        'time_played': stats[2]['value'],
        'kills': kills,
        'deaths': deaths,
        'kd': round(kills / deaths, 2),
        'kd_total': None,
        'kd_fraction': None,
        'wins': stats[5]['value'],
        'headshots': None,
        'headshotpct': None,
        'headshot_percentile': None,
        'kd_percentile': None,
        'wl_percentage': None,
        'wl_percentile': None
    }
    return return_dict


def request_steam_csgo_stats(steam_id=76561199056418213):
    resp = requests.get(
        url=f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key={STEAM_WEB_API_KEY}&steamid={steam_id}'
    )

    return resp
