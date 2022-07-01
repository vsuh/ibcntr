from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from ibcntr.conf import Config

db = SQLAlchemy()
app = None

def create_app():
    global app
    app = Flask(__name__)
    app.config.from_object(Config)
   
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
        
    from .models import User
    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .bats import bats as bats_blueprint
    app.register_blueprint(bats_blueprint)

    return app


