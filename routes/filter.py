from flask import Flask, make_response, render_template, jsonify
import requests
import app
from  controllers.kong_filter import get_paths
# @app.route('/paths', methods=['GET'])
# def aaa():
#     get_paths()

from flask import Blueprint
from  controllers.kong_filter import get_paths

auth_bp = Blueprint('auth_bp', __name__)
auth_bp.route('/paths', methods=['GET'])(get_paths)