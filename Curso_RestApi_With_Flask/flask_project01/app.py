import os
import secrets # se puede usar para generar una llave para el token random.
from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

# importamos la base de datos db ( que es SQLAlchemy )
from db import db
from blocklist import BLOCKLIST
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
    migrate = Migrate(app, db) # flask-migrate ayuda a crear las tablas para la base de datos.
    api = Api(app)
    
    # una buena forma de generar el secret key app.config["JWT_SECRET_KEY"] = secrets.SystemRandom().getrandbits(128) < el problema es que se cambiara siempre, es mejor generarla y guardarla. 
    app.config["JWT_SECRET_KEY"] = "Dairan" # set secret key (is used for signing JWT). Mejor guardar en un ENV
    jwt = JWTManager(app)
    

    
    # al usuario hacer logout, su token se almacena en el blocklist y es inválido para ingresar como el usuario ( debe crear otro JWT).
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload): # revisa si el token esta en el BLOCKLIST.
        return jwt_payload["jti"] in BLOCKLIST
    
    
    @jwt.revoked_token_loader # Este es el mensaje que se recibe si el token esta en el BLOCKLIST.
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify (
                {
                    "description": "The token has been revoked.",
                    "error": "token_revoked"
                }
            ),
            401,
        )
    
    
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify (
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required"
                }
            ),
            401,
        )
    
    #los claims son para añádir información extra en un token
    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity): # este identity es el que se crea cuando se firma nuestro token (es el id el usuario en este caso).
        # en esta comparación se buscaría mejor en la base de datos y revisaría si el user es admin.
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}
    
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"message": "The token has expired.", "error": "token_expired"}
                ),
            401,
        )
    
    @jwt.invalid_token_loader # con esto obligamos al usuario a pasar el jwt que recibe al hacer el login desde el header en Authorization: Bearer -token
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401
        )
        
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify (
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )
        
    
    
    # esto no es necesario ya con SQLAlchemy por que Flask-Migrate crea las tablas de nuestra base de datos.
    # with app.app_context(): # esto se ejecuta al hacer un primer request, esto crea todas las tablas en la base de datos.
    #     db.create_all() # si existen tablas, no se ejecuta. (crea el daba.db en el directorio instance)

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)
    
    
    return app