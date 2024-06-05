import os
import secrets # se puede usar para generar una llave para el token random.
from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from db import db
import models
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint
from resources.user import blp as UserBlueprint


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DABASE_URL", "sqlite:///data.db") # crea un archivo data.db
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app) # inicializa la extension SQL alchemy de flask recibiendo nuestra app.


    api = Api(app)
    
    # una buena forma de generar el secret key app.config["JWT_SECRET_KEY"] = secrets.SystemRandom().getrandbits(128) < el problema es que se cambiara siempre, es mejor generarla y guardarla. 
    app.config["JWT_SECRET_KEY"] = "Dairan" # set secret key (is used for signing JWT). Mejor guardar en un ENV
    jwt = JWTManager(app)
    
    with app.app_context(): # esto se ejecuta al hacer un primer request, esto crea todas las tablas en la base de datos.
        db.create_all() # si existen tablas, no se ejecuta. (crea el daba.db en el directorio instance)

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)
    
    
    return app