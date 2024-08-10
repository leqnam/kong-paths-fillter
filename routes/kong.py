
from flask import Flask, make_response, render_template, jsonify, request
from controllers.kong import get_svc, get_paths, get_ports
from controllers.apicontroller import create_yaml, update_yaml, delete_yaml

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/paths', methods=['GET'])
    def paths():
        return get_paths()
    
    @app.route('/ports', methods=['GET'])
    def ports():
        return get_ports()
    
    @app.route('/svc', methods=['POST'])
    def svc():
        return create_yaml()
    
    @app.route('/svc/<helm_id>', methods=['PUT'])
    def putsvc(helm_id):
        return update_yaml(helm_id)
    
    @app.route('/svc/<helm_id>', methods=['DELETE'])
    def delsvc(helm_id):
        return delete_yaml(helm_id)
