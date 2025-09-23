from flask import request, render_template, redirect, url_for, session
import os
from services.prediction_service import PredictionService
from utils.db_utils import csv_to_db

# Initialize prediction service
prediction_service = PredictionService()

def register_routes(app):
    """Register all application routes"""
    
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/predict', methods=['GET', 'POST'])
    def predict():
        if request.method == 'POST':
            try:
                # Preprocess form data
                df = prediction_service.preprocess_data(request.form)
                
                # Make prediction
                prediction = prediction_service.predict(df)
                
                # Extract metric values
                ptp = df['PTP_rate'].round(2).values[0]
                rpc = df['RPC_rate'].round(2).values[0]
                recovery_rate = df['recovery_rate'].round(2).values[0]
                
                # Get metric descriptions
                descriptions = prediction_service.get_metric_descriptions(ptp, rpc, recovery_rate)
                
                # Generate charts
                charts = prediction_service.generate_charts(rpc, ptp, recovery_rate)
                
                return render_template('result.html', 
                                       prediction=prediction[0], 
                                       ptp=ptp, 
                                       rpc=rpc, 
                                       recovery_ratio=recovery_rate,
                                       ptp_description=descriptions['ptp'],
                                       rpc_description=descriptions['rpc'],
                                       recovery_ratio_description=descriptions['recovery'],
                                       radar_data=charts['radar'], 
                                       rpc_data=charts['rpc'], 
                                       ptp_data=charts['ptp'], 
                                       recovery_ratio_data=charts['recovery']
                                      )
            except Exception as e:
                return f"Error processing request: {str(e)}"
        else:
            return render_template('prediction.html')
    
    @app.route('/analysis', methods=['GET', 'POST'])
    def analysis():
        if request.method == 'POST':
            file = request.files['file']
            if file and file.filename.endswith('.csv'):
                # Save the file
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(file_path)
                
                # Import to database
                if csv_to_db(file_path):
                    session['uploaded'] = True
                    return redirect(url_for('dashboard'))
                else:
                    return "Error importing data"
        return render_template('upload.html')
    
    @app.route('/dashboard')
    def dashboard():
        if not session.get('uploaded'):
            return redirect(url_for('analysis'))
        return render_template('analytics.html')
    
    # Add more routes as needed