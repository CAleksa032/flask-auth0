from flask import Flask
from dotenv import find_dotenv, load_dotenv
from os import environ as env
from authlib.integrations.flask_client import OAuth
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")

oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)

from flask_app.auth0 import auth0_blueprint
app.register_blueprint(auth0_blueprint)
