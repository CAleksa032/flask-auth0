from flask_app import app
from os import environ as env

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=env.get("PORT", 3000))