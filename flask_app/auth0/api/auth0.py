from flask_app.auth0 import auth0_blueprint
from flask_app import oauth
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
from flask import redirect, render_template, session, url_for


# Controllers API
@auth0_blueprint.route("/")
def home():
    return render_template(
        "home.html",
        session=session.get("user"),
        pretty=json.dumps(session.get("user"), indent=4),
    )


@auth0_blueprint.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")


@auth0_blueprint.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("auth0.callback", _external=True)
    )


@auth0_blueprint.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )