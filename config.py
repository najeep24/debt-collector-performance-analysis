import os

class Config:
    # Application settings
    SECRET_KEY = 'your_secret_key'  # Replace with a strong, unique key in production
    DEBUG = True
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/dashboard_data'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # File upload settings
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size
    ALLOWED_EXTENSIONS = {'csv'}