from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'auth.login'

from views import main, auth

app.register_blueprint(main.bp)
app.register_blueprint(auth.bp)

if __name__ == '__main__':
    app.run(debug=True)
