from flask import Flask
from .extensions import db, bcrypt, jwt
from .routes import main
from .auth import auth   

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(auth)   

    return app