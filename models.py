def process_json_data(data):
    platforminfo = data['platformInfo']
    stats = data['segments'][0]['stats']

    return_dict = {
        'avatar_url': platforminfo['avatarUrl'],
        'username': platforminfo['platformUserHandle'],
        'time_played': stats['timePlayed']['displayValue'],
        'kills': stats['kills']['value'],
        'deaths': stats['deaths']['value'],
        'kd': round(stats['kd']['value'], 2),
        'wl': stats['wlPercentage']['value'],
        'kd_percentile': stats['kd']['percentile'],
        'kd_total': round(stats['kd']['value'], 2) + 1.00,
        'kd_fraction': round(stats['kd']['value'] / (stats['kd']['value'] + 1.00), 2) * 100
    }

    return return_dict
