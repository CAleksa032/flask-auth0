from flask import Blueprint

APP_NAME = 'auth0'
auth0_blueprint = Blueprint(APP_NAME, __name__)

import flask_app.auth0.api
