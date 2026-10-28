import os
from dotenv import load_dotenv

# Load environment variables from a .env file if present
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(os.path.dirname(basedir), '..', '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-fallback-secret-key')
    
    # Ensure psycopg2 is used for PostgreSQL connections
    db_url = os.environ.get('DATABASE_URL', 'postgresql://postgres:password@localhost:5433/cultural_roots')
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)
        
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False