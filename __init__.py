import pathlib
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = pathlib.Path(__file__).parent.resolve()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__,
        template_folder="templates",
        static_folder="static")
    
    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            'DATABASE_URL', 'postgresql://kong:kong@localhost:5432/kong'
        )  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Import routes explicitly
    from routes.filter import register_routes

    # Register the routes with the app
    register_routes(app)

    return app

