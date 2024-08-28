# Check if Python is installed
if (-Not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Output "Python is not installed. Installing Python..."
    Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe -OutFile python-installer.exe
    Start-Process -FilePath python-installer.exe -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
    Remove-Item python-installer.exe
} else {
    Write-Output "Python is already installed."
}

# Check if pip is installed
if (-Not (Get-Command pip -ErrorAction SilentlyContinue)) {
    Write-Output "pip is not installed. Installing pip..."
    python -m ensurepip --upgrade
} else {
    Write-Output "pip is already installed."
}

# Update pip to the latest version
python -m pip install --upgrade pip

# Install required packages
pip install llama-index openai pypdf python-dotenv streamlit langchain langchain_community langchain-openai

Write-Output "All packages have been installed successfully!"

