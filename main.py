from flask import Flask, jsonify
import pandas as pd
import os
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'sample_data.csv')
# Create a Flask app (this is our web server)
app = Flask(__name__)

# Path to our CSV file
DATA_FILE = 'sample_data.csv'
LOG_FILE = '../logs/processing.log'

# Function to write logs
def log_message(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")

# ENDPOINT 1: Process and return data
@app.route('/data', methods=['GET'])
def get_data():
    """
    Reads CSV, calculates statistics, returns JSON
    This simulates a data processing app
    """
    try:
        # Read the CSV file using pandas
        df = pd.read_csv(DATA_FILE)
        
        # Calculate some statistics
        stats = {
            'total_employees': len(df),
            'average_salary': float(df['salary'].mean()),
            'average_age': float(df['age'].mean()),
            'highest_salary': float(df['salary'].max()),
            'employees': df.to_dict('records')  # Convert to list of dicts
        }
        
        # Log this processing
        log_message(f"Processed {len(df)} records successfully")
        
        return jsonify(stats), 200
    
    except Exception as e:
        log_message(f"ERROR: {str(e)}")
        return jsonify({'error': str(e)}), 500

# ENDPOINT 2: Health check / status
@app.route('/status', methods=['GET'])
def status():
    """
    Shows the platform is running and displays logs
    """
    try:
        # Read last 10 lines of log
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r') as f:
                logs = f.readlines()[-10:]  # Last 10 lines
        else:
            logs = ["No logs yet"]
        
        return jsonify({
            'status': 'running',
            'timestamp': datetime.now().isoformat(),
            'recent_logs': logs
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ENDPOINT 3: Simple health check
@app.route('/health', methods=['GET'])
def health():
    """
    Basic health check - is the app alive?
    """
    return jsonify({'status': 'healthy'}), 200

# Run the app
if __name__ == '__main__':
    log_message("Application started")
    app.run(host='0.0.0.0', port=5000, debug=True)
