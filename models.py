import os
import requests
from dotenv import load_dotenv


load_dotenv()
STEAM_WEB_API_KEY = os.environ.get("STEAM_WEB_API_KEY")


def process_json_data(csgo_data, player_data):
    player_data = player_data['response']['players'][0]
    stats = csgo_data['playerstats']['stats']
    kills = stats[0]['value']
    deaths = stats[1]['value']
    kd = round(kills / deaths, 2)
    return_dict = {
        'avatar_url': player_data['avatar'],
        'username': player_data['personaname'],
        'time_played': stats[2]['value'],
        'kills': kills,
        'deaths': deaths,
        'kd': kd,
        'kd_fraction': round(kd / (kd + 1.00), 2) * 100,
        'wins': stats[5]['value'],
        'headshots': stats[23]['value'],
    }
    return return_dict


def request_steam_csgo_stats(steam_id):
    resp = requests.get(
        url=f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key={STEAM_WEB_API_KEY}&steamid={steam_id}'
    )

    return resp


def request_steam_player_summary(steam_id):
    resp = requests.get(
        url=f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={STEAM_WEB_API_KEY}&steamids={steam_id}'
    )

    return resp
