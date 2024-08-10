from flask import Flask, make_response, render_template, jsonify, request, abort
import subprocess, yaml, os, uuid, base64, json
from tempfile import NamedTemporaryFile
from services.yaml_convert import custom_yaml_file, json_to_yaml
from services.db_action import create_kong, update_kong, delete_kong
from services.git_action import git_action
from collections import OrderedDict
from subprocess import check_output
from dotenv import load_dotenv
from __init__ import db
from models.kong import kong_model
from sqlalchemy.exc import SQLAlchemyError 
# import ruamel.yaml
# import json

load_dotenv()
git_url = os.getenv('GIT_URL')
print(git_url)

def create_yaml():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Invalid content type. Please send JSON data.'}), 400

    try:
        json_data = request.get_json()
        json_parser = json_to_yaml(json_data)

        # return yaml_data, 200, {'Content-Type': 'text/yaml'}
        with NamedTemporaryFile(mode='w', suffix='.yaml') as values_file:
            values_file.write(json_parser)
            values_file.flush()

            # Call the Helm rendering function
            helm_output, status_code = render_helm_template(
                values_file.name,
                './kong-chart'  # Replace with your chart directory
            )

            if status_code == 200:
                    # with open(values_file.name, 'r') as f:
                    #     yaml_content = f.read()
                # git_act = git_action(git_url, 'create', helm_output)  # Pass content 
                # return git_act
                helm_dict = yaml.safe_load(helm_output)
                helm_id = helm_dict.get('id', str(uuid.uuid4()))
                service_name = helm_dict['services'][0].get('name','missing')
                new_yaml_entry, status_code = create_kong(helm_id, service_name, base64.b64encode(helm_output.encode()).decode())
                return(new_yaml_entry), status_code
#                 return jsonify({'message': 'Kong data config sucessfully create !!!', 'id': new_yaml_entry }), 201
# #                 return jsonify({'message': 'Data inserted successfully!', 'id': new_entry.id}), 201
# # #                return(helm_output)
    except yaml.YAMLError as e:
        return jsonify({'error': f'Error converting to YAML: {e}'}), 500
    except Exception as e:
        return jsonify({'error': f'An error occurred: {e}'}), 500


def update_yaml(helm_id):
    if request.content_type != 'application/json':
        return jsonify({'error': 'Invalid content type. Please send JSON data.'}), 400

    try:
        json_data = request.get_json()
        json_parser = json_to_yaml(json_data)

        # return yaml_data, 200, {'Content-Type': 'text/yaml'}
        with NamedTemporaryFile(mode='w', suffix='.yaml') as values_file:
            values_file.write(json_parser)
            values_file.flush()

            # Call the Helm rendering function
            helm_output, status_code = render_helm_template(
                values_file.name,
                './kong-chart'  # Replace with your chart directory
            )

            if status_code == 200:
                    # with open(values_file.name, 'r') as f:
                    #     yaml_content = f.read()
                # git_act = git_action(git_url, 'create', helm_output)  # Pass content 
                # return git_act
                update_yaml_entry, status_code = update_yaml(helm_id, base64.b64encode(helm_output.encode()).decode())
                return(update_yaml_entry), status_code
                
#                 return jsonify({'message': 'Kong data config sucessfully create !!!', 'id': new_yaml_entry }), 201
# #                 return jsonify({'message': 'Data inserted successfully!', 'id': new_entry.id}), 201
# # #                return(helm_output)
    except yaml.YAMLError as e:
        return jsonify({'error': f'Error converting to YAML: {e}'}), 500
    except Exception as e:
        return jsonify({'error': f'An error occurred: {e}'}), 500
def delete_yaml(helm_id):
    delete_yaml_entry, status_code = delete_kong(helm_id)
    return(delete_yaml_entry), status_code

def render_helm_template(values_file_path, chart_directory):
    try:
        helm_output = check_output(['helm', 'template','--values', values_file_path, chart_directory]).decode('utf-8')
        return helm_output, 200
    except subprocess.CalledProcessError as e:
        return jsonify({'error': f'Helm template command failed: {e.output}'}), 500
    