from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os
from config import Config
from transformers.feature_transformer import ProblemSolvingTransformer
from transformers.feature_transformer import FeedbackTransformer
from transformers.feature_transformer import RPCTransformer
from transformers.feature_transformer import CEITransformer
from transformers.feature_transformer import PTPTransformer
from transformers.feature_transformer import ZScoreTransformer
from transformers.feature_transformer import DataTypeTransformer

# Initialize the application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db = SQLAlchemy(app)

# Import routes after app is created to avoid circular imports
from routes import register_routes

# Register all application routes
register_routes(app)

if __name__ == '__main__':
    # Ensure upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=app.config['DEBUG'])