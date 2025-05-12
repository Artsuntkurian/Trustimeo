from flask import Blueprint, request, render_template, jsonify, url_for, send_file
from werkzeug.utils import secure_filename
import os
from app.model.predict import load_model, predict_video

# Initialize Blueprint
main = Blueprint('main', __name__)

# Load the model, transform, and device
model, transform, device = load_model()

@main.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads and return prediction results."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        upload_folder = os.path.join('app', 'uploads')
        filepath = os.path.join(upload_folder, filename)

        # Ensure the upload folder exists
        os.makedirs(upload_folder, exist_ok=True)
        file.save(filepath)

        # Debugging: Check if the file was saved successfully
        if not os.path.exists(filepath):
            return jsonify({'error': 'File could not be saved'}), 500

        # Run prediction on the uploaded file
        result = predict_video(filepath, model, transform, device)

        # Generate the URL for the uploaded file
        video_url = url_for('main.uploaded_file', filename=filename, _external=True)

        # Return the result and file URL
        return jsonify({'result': result, 'videoUrl': video_url})

@main.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded files."""
    full_path = os.path.join(os.getcwd(), 'app', 'uploads', filename)

    # Check if the file exists
    if not os.path.exists(full_path):
        return "File not found", 404

    # Serve the file
    return send_file(full_path)