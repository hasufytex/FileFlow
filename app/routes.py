from flask import Blueprint, render_template, request, send_from_directory, current_app
import os

main = Blueprint('main', __name__)

# Home page
@main.route('/')
def home():
    return render_template('home.html')

# Display downloadable files
@main.route('/download')
def download():
    files = os.listdir(current_app.config['DOWNLOAD_FOLDER'])
    file_info = [
        {"name": file, "size": os.path.getsize(os.path.join(current_app.config['DOWNLOAD_FOLDER'], file))}
        for file in files
    ]
    return render_template('download.html', files=file_info)

# Handle file download
@main.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(current_app.config['DOWNLOAD_FOLDER'], filename)

# Upload form
@main.route('/upload')
def upload_form():
    return render_template('upload.html')

# Handle file upload
@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename))
    return f'File "{file.filename}" uploaded successfully!'

@main.route('/list_all_files')
def list_all_files():
    upload_folder = current_app.config['UPLOAD_FOLDER']
    download_folder = current_app.config['DOWNLOAD_FOLDER']

    upload_files = [
        {"name": file, "size": os.path.getsize(os.path.join(upload_folder, file))}
        for file in os.listdir(upload_folder)
    ]
    
    download_files = [
        {"name": file, "size": os.path.getsize(os.path.join(download_folder, file))}
        for file in os.listdir(download_folder)
    ]

    # Combine the lists
    all_files = {"uploads": upload_files, "downloads": download_files}
    
    return render_template('list_all_files.html', all_files=all_files)
