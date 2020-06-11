def process_json_data(data):
    platforminfo = data['platformInfo']

    return_dict = {
        'avatar_url': platforminfo['avatarUrl'],
        'username': platforminfo['platformUserHandle']
    }

    return return_dict
