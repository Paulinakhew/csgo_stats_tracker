def process_json_data(data):
    platforminfo = data['platformInfo']
    stats = data['segments'][0]['stats']

    return_dict = {
        'avatar_url': platforminfo['avatarUrl'],
        'username': platforminfo['platformUserHandle'],
        'time_played': stats['timePlayed']['displayValue'],
        'kills': stats['kills']['value'],
        'deaths': stats['deaths']['value'],
        'kd': round(stats['kd']['value'], 2)
    }

    return return_dict
