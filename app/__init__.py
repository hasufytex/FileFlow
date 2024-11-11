from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Configuration settings
    app.config['UPLOAD_FOLDER'] = os.path.join('instance', 'uploads')
    app.config['DOWNLOAD_FOLDER'] = os.path.join('instance', 'downloads')

    # Create directories if they don't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['DOWNLOAD_FOLDER'], exist_ok=True)

    # Import routes
    from app.routes import main
    app.register_blueprint(main)

    return app