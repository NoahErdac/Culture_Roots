from flask import Flask
from .config import Config
from .extensions import db, migrate, cors
from app.api.public_api import public_bp
from app.api.contribute_api import contribute_bp
from app.api.admin_api import admin_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Configure CORS to allow frontend requests (e.g., React on port 3000) 
    # to access any route under /api/
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

   # Register Blueprints
    from app.api.public_api import public_bp
    from app.api.contribute_api import contribute_bp
    from app.api.admin_api import admin_bp

    app.register_blueprint(public_bp, url_prefix='/api')
    app.register_blueprint(contribute_bp, url_prefix='/api')
    app.register_blueprint(admin_bp, url_prefix='/api')

    @app.route('/api/health')
    def health_check():
        return {"status": "healthy", "database": "PostgreSQL configured"}

    return app