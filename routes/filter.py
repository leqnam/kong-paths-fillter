from flask import Flask, make_response, render_template, jsonify
import requests
import os
from flask import render_template, jsonify
import requests
import os
from controllers.kong_filter import get_paths

def register_routes(app):
    @app.route('/paths', methods=['GET'])
    def paths():
        return get_paths()

    @app.route('/')
    def index():
        return render_template('index.html')
