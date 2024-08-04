from flask import Flask, make_response, render_template, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.headers['X-Powered-By'] = 'namlq01'
    return resp

if __name__ == '__main__':
    app.run(debug=True)
