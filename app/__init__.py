from flask import Flask
import os

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['UPLOAD_FOLDER'] = 'app/uploads/'
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
