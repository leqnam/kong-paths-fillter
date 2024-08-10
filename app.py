from flask import Flask, make_response, render_template, jsonify, request
import requests
import os
from dotenv import load_dotenv
from controllers.kong import get_paths
from routes.kong import ports_bp, paths_bp, svc_bp
from __init__ import create_db_connect

# app = Flask(__name__)
app = create_db_connect()

app.register_blueprint(ports_bp) 
app.register_blueprint(paths_bp) 
app.register_blueprint(svc_bp) 
@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    return resp

if __name__ == '__main__':
    app.run(debug=True)
