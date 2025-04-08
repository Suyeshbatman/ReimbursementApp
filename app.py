from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///receipts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'pdf'}

db = SQLAlchemy(app)

# Create the receipts table
class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)

# Create all tables within the app context
with app.app_context():
    db.create_all()  # Create the database table if it doesn't exist

# Utility function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Home route to render the HTML form
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint to submit a receipt
@app.route('/api/receipts/submit', methods=['POST'])
def submit_receipt():
    if 'receiptFile' not in request.files:
        return jsonify({"message": "No file part"}), 400
    
    file = request.files['receiptFile']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        data = request.form
        receipt = Receipt(
            date=data['date'],
            amount=data['amount'],
            description=data['description'],
            file_name=filename
        )
        
        db.session.add(receipt)
        db.session.commit()
        
        return jsonify({"message": "Receipt submitted successfully!"}), 201

    return jsonify({"message": "Invalid file type"}), 400

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
