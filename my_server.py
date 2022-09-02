from flask import Flask, request, abort
import pandas as pd

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # print(request.json)
        data = request.json
        download_url = data['data']['downloadUrl']
        print(download_url)
        return '[accepted]', 200
    else:
        abort(400)
    


if __name__ == '__main__':
    app.run(host='0.0.0.0')