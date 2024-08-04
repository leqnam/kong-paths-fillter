from flask import Flask, make_response, render_template, jsonify
import requests
import os

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        return None