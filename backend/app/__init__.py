from flask import Flask
from .config import Config
from .extensions import db, migrate, cors

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Configure CORS to allow frontend requests (e.g., React on port 3000) 
    # to access any route under /api/
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

    # Placeholder for future API blueprint registration
    # from .api.public_api import public_bp
    # app.register_blueprint(public_bp, url_prefix='/api')

    @app.route('/api/health')
    def health_check():
        return {"status": "healthy", "database": "PostgreSQL configured"}

    return app