from flask import Flask, make_response, render_template, jsonify, request, abort
from __init__ import db
from models.kong import kong_model
from sqlalchemy.exc import SQLAlchemyError 

def create_kong(helm_id, service_name, yaml):
    # id = str(uuid.uuid4())
    try:
        new_yaml = kong_model(
                            id             = helm_id,
                            service_name   = service_name,
                            yaml           = yaml
                            )
        db.session.add(new_yaml)
        db.session.commit()
        response = kong_model.query.get(helm_id).toDict()
        # response['yaml'] = base64.b64decode(response['yaml']).decode()
        # yaml_data = base64.b64decode(response['yaml']).decode()
        # parsed_yaml = yaml.safe_load(yaml_data)
        # response['yaml'] = json.dumps(parsed_yaml)
        return jsonify(response),201
    except SQLAlchemyError as e:
        # Handle database errors here 
        db.session.rollback()  # Important: Rollback the session
        print(str(e))  # Log the error for debugging 
        abort(500, description="Failed to save to the database.")

def update_kong(helm_id,yaml):
    try:
        yaml_file = kong_model.query.get(helm_id)
        yaml_file.yaml = yaml
        db.session.commit()
        response = kong_model.query.get(helm_id).toDict()
        return jsonify(response),200
    except SQLAlchemyError as e:
        db.session.rollback()  # Important: Rollback the session
        print(str(e))  # Log the error for debugging 
        abort(500, description="Failed to update to the database.")

def delete_kong(helm_id):
    try:
        kong_instance = kong_model.query.get(helm_id)
        if kong_instance:
           db.session.delete(kong_instance) 
           db.session.commit()
           return jsonify({'message': 'Kong record deleted successfully'}), 200
        else:
            return jsonify({'message': 'Kong record not found'}), 404
    except SQLAlchemyError as e:
        db.session.rollback()  # Important: Rollback the session
        print(str(e))  # Log the error for debugging 
        abort(500, description="Failed to delete record.")