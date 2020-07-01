from flask import Flask, render_template, redirect
import models as m


app = Flask(__name__)


@app.route('/', methods=['GET'])
def dashboard():
    return redirect('/76561199056418213')


@app.route('/<steam_id>')
def user_dashboard(steam_id):
    resp = m.request_steam_csgo_stats(steam_id=steam_id)
    user_info = m.request_steam_player_summary(steam_id=steam_id)

    if resp.status_code == 200 and user_info.status_code == 200:
        csgo_data = resp.json()
        player_data = user_info.json()
        return_dict = m.process_json_data(csgo_data=csgo_data, player_data=player_data)
        return render_template(
            'dashboard.html',
            data=return_dict,
        )
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
