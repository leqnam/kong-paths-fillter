from flask import Flask, make_response, render_template, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

api_urls = os.getenv('API_URLS').split(',')

print(api_urls)

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        return None

@app.route('/paths', methods=['GET'])
def get_paths():
    all_data = []
    for api_url in api_urls:
        data = fetch_data(api_url)
        if data:
            for entry in data:
                for path in entry.get('paths', []):
                        all_data.append({'url': api_url, 'path': path})
    resp = make_response(jsonify(all_data))
    resp.headers['X-Powered-By'] = 'namlq01'
    return resp

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.headers['X-Powered-By'] = 'namlq01'
    return resp

if __name__ == '__main__':
    app.run(debug=True)
