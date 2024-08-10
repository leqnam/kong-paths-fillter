import pathlib
from flask import Flask
from dotenv import load_dotenv

basedir = pathlib.Path(__file__).parent.resolve()

def create_app():
    app = Flask(__name__,
        template_folder="templates",
        static_folder="static")
    
    load_dotenv()

    # Import routes explicitly
    from routes.filter import register_routes

    # Register the routes with the app
    register_routes(app)

    return app
