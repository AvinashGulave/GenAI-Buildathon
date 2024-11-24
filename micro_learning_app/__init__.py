from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object('micro_learning_app.config.Config')
    
    db.init_app(app)
    login.init_app(app)
    
    with app.app_context():
        from . import models
        db.create_all()
        
        from .views import main, auth
        app.register_blueprint(main.bp)
        app.register_blueprint(auth.bp)
        
        # Error handlers
        @app.errorhandler(404)
        def not_found_error(error):
            return render_template('404.html'), 404

        @app.errorhandler(500)
        def internal_error(error):
            db.session.rollback()
            return render_template('500.html'), 500
        
        return app
