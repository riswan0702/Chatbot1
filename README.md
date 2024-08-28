# AI CHATBOT USING PYINSTALLER AND STREAMLIT

## PROJECT OVERVIEW

#### PURPOSE: 
A document-based AI chatbot designed to answer user queries, built with Streamlit and packaged as a standalone executable.

#### TECH STACK: 
Python, Streamlit, PyInstaller.

## TABLE OF CONTENTS

#### 1. Installation
#### 2. Usage
#### 3. Creating Executable
#### 4. Features
#### 5. Files
#### 6. License
#### 7. Contact
   
## INSTALLATION

#### 1. Clone the Repository
#### 2. Install Depedencies:
Run the *setup.ps1* Power Shell Script to install all the dependencies
#### 3. Secrets.toml File Creation
Create a *secrets.toml* file in a folder *.streamlit* which has the API Key required.
#### 3. Run the Application
  ```bash
python run.py
```

## USAGE

#### Launching the Chatbot:
Run the app using *python run.py*

#### Interaction:
1. Upload documents in supported formats (PDF, DOCX, TXT).
2. Ask questions related to the uploaded documents directly via the chatbot interface.


## CREATING EXECUTABLE

#### 1. Install PyInstaller (if not already installed):
  ```bash
pip install pyinstaller
```

#### 2. Create Executable:
-Use PyInstaller to convert the run.py into an executable:
  ```bash
pyinstaller --onefile run.py
```
The resulting .exe file will be located in the dist folder.
Make sure your *Bot.py* and *run.py* along with *.streamlit* folder is copied to the same *dist* folder.

## FEATURES
#### 1. Interactive UI: 
Built using Streamlit.
#### 2. Document-Based Q&A: 
Provides answers based on the content of uploaded documents.
#### 3. Standalone Executable: 
Packaged as a single .exe file using PyInstalle

## FILES
#### *bot.py*: 
Contains the main chatbot logic, including context creation, user interaction handling, and AI response generation.
#### *run.py*: 
Wrapper code to run the Streamlit app, used for creating the executable with PyInstaller.
#### *requirements.txt*:
List of Python dependencies required for the project.
#### *static/*:
Contains images, such as screenshots or logos, used in the application or documentation.
#### *data/*:
Directory where document files for context creation are stored.
#### *archives/*:
Directory where archived log files are stored.
#### *storage/*:
Directory for persistent storage of AI model context.

## LICENSE

[MIT](https://choosealicense.com/licenses/mit/)

## CONTACT

Devadathan E K
#### devadathan525@gmail.com

#### Project Link:
https://github.com/yourusername/ai-chatbot-pyinstaller-streamlit
