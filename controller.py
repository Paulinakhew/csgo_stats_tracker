from flask import Flask, render_template, redirect
import models as m


app = Flask(__name__)


@app.route('/', methods=['GET'])
def dashboard():
    return redirect('/76561199056418213')

@app.route('/<steam_id>')
def user_dashboard(steam_id):
    resp = m.request_steam_csgo_stats(steam_id=steam_id)

    if resp.status_code == 200:
        data = resp.json()
        return_dict = m.process_json_data(data=data)
        return render_template(
            'dashboard.html',
            data=return_dict,
        )
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
