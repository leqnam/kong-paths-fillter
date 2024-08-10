
from flask import Flask, make_response, render_template, jsonify, request
import requests
from controllers.kong import get_svc, get_paths, get_ports
from controllers.apicontroller import create_yaml, update_yaml, delete_yaml
from flask import Blueprint

ports_bp = Blueprint('ports_bp', __name__)
ports_bp.route('/ports', methods=['GET'])(get_ports)

paths_bp = Blueprint('paths_bp', __name__)
paths_bp.route('/paths', methods=['GET'])(get_paths)

svc_bp = Blueprint('svc_bp',__name__)
svc_bp.route('/svc', methods=['POST'])(create_yaml)

@svc_bp.route('/svc/<helm_id>', methods=['PUT','DELETE'])
def yaml_action(helm_id):
    if request.method == 'PUT':  
        return update_yaml(helm_id)
    if request.method == 'DELETE':
        return delete_yaml(helm_id)
    else: 
        return 'Method is not allowed !!!!', 405
    


