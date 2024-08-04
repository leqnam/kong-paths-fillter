from flask import Flask, make_response, render_template, jsonify
import requests
import os
from dotenv import load_dotenv
from services.kong import fetch_data


load_dotenv()
api_urls = os.getenv('API_URLS').split(',')

print(api_urls)

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