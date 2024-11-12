# Flask File Upload and Download Application

This is a simple Flask web application that allows users to upload files to the server and download files from predefined directories. The app uses Tailwind CSS for styling and provides a clean, responsive interface.

Transferring files to and from an Apple iPhone can often be a challenging process, so I developed a simple application to address this issue—something Apple has yet to offer. The application only requires both the device and the computer to be on the same network. With proper port forwarding, it should also function outside the local network. Please note, I am not responsible for any security vulnerabilities that may arise from using or adapting this example code.

## Features
- **File Upload**: Allows users to upload files to the server.
- **File Download**: Lists available files for download from a predefined folder.
- **View Both Folders**: View files from both the upload and download directories.

## Requirements
- Python 3.x
- Flask

## Setup

### 1. Clone the Repository
Start by cloning the project to your local machine:

```bash
git clone https://github.com/hasufytex/FileFlow.git
cd FileFlow
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3. Run the Application

```bash
python run.py
```

By default, the app will run on http://127.0.0.1:8000/
##
While this application is a simple demonstration of file transfers, it is important to note that it is not production-ready!