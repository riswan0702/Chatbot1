# AI CHATBOT USING PYINSTALLER AND STREAMLIT

## Project Overview 

#### Purpose: 
A document-based AI chatbot designed to answer user queries, built with Streamlit and packaged as a standalone executable.

#### Tech Stack: 
Python, Streamlit, PyInstaller.

## Table of Contents

1. Installation
2. Usage
3. Creating Executable
4. Features
5. File Structure
6. Configuration
7. Contributing
8. License
9. Contact
   
## Installation

### 1. CLONE THE REPOSITORY
### 2. INSTALL DEPENDENCIES:
Run the *setup.ps1* Power Shell Script to install all the dependencies
### 3. RUN THE APPLICATION
  ```bash
python run.py
```

## Usage

### Launching the Chatbot:
Run the app using *python run.py*

### Interaction:
1. Upload documents in supported formats (PDF, DOCX, TXT).
2. Ask questions related to the uploaded documents directly via the chatbot interface.


## CREATING EXECUTABLE

### 1. Install PyInstaller (if not already installed):
  ```bash
pip install pyinstaller
```

### 2. Create Executable:
-Use PyInstaller to convert the run.py into an executable:
  ```bash
pyinstaller --onefile run.py
```
The resulting .exe file will be located in the dist folder.

## License

[MIT](https://choosealicense.com/licenses/mit/)
