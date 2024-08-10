import yaml
from flask import Flask, request, jsonify
from collections import OrderedDict
# app = Flask(__name__)

def custom_yaml_file(data, indent=2):
    lines = []
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"{' ' * indent}- {item}")
        else:
            lines.append(f"{key}: {value}")
    return "\n".join(lines)

def json_to_yaml(json_data):
    yaml_data = yaml.dump(json_data, indent=2)
    return(yaml_data)