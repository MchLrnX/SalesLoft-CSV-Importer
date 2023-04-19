# SalesLoft CSV Importer

A web application that automates the process of uploading a CSV file to SalesLoft using Python, Selenium, and Flask. It allows users to schedule the CSV import process to run daily at a specified time and provides an intuitive web interface.

## Features

- Intuitive web interface for CSV file path input and scheduling
- Daily import process scheduling at specified time
- Automated login and import process using Selenium
- Secure storage of user credentials using .env file
- Responsive design with Bootstrap
- Compatibility with Intel, ARM, and AMD processors
- Works on Windows, Mac, and Ubuntu

## Prerequisites

- Python 3.6 or higher
- Google Chrome browser
- Conda (Miniconda or Miniforge)

## Installation

### 1. Install Conda

Follow the instructions for your operating system and processor:

#### Intel and AMD Processors:

- Windows and Ubuntu: [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Mac: [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

#### Apple M1 (ARM):

- Mac: [Miniforge](https://github.com/conda-forge/miniforge#miniforge3)
- Ubuntu on Mac M1: [Miniforge](https://github.com/conda-forge/miniforge#miniforge3)

### 2. Clone the repository:

git clone https://github.com/MchLrnX/salesloft_csv_importer.git

3. Navigate to the project directory:

cd salesloft_csv_importer

4. Create a new Conda environment with Python 3.9:

conda create -n salesloft_csv_importer python=3.9

5. Activate the new environment:

conda activate salesloft_csv_importer

6. Install the required packages:

pip install -r requirements.txt

7. Add your SalesLoft username and password to the .env file:
makefile

USERNAME=your_salesloft_username
PASSWORD=your_salesloft_password
Make sure to replace your_salesloft_username and your_salesloft_password with your actual SalesLoft credentials.

8. Run the application:
python app.py

The application will be available at http://127.0.0.1:5000/ in your web browser.

Usage
Access the web interface at http://127.0.0.1:5000/.
Enter the CSV file path and the time you want to schedule the import process.
Click "Submit" to schedule the import process. You will be redirected to a success page, confirming the import has been scheduled.
Creating Launch Scripts
To make it easy to launch the application with a double-click, you can create a script for your operating system:

Windows
Create a new text file and name it
"launch_salesloft_csv_importer.bat".

2. Open the file and add the following lines:

@echo off
conda activate salesloft_csv_importer
python app.py
pause

3. Save the file and double-click it to launch the application.

### Mac and Ubuntu

1. Create a new text file and name it "launch_salesloft_csv_importer.sh".
2. Open the file and add the following lines:

```bash
#!/bin/bash
source activate salesloft_csv_importer
python app.py

Save the file and make it executable with the following command:
chmod +x launch_salesloft_csv_importer.sh

Double-click the file to launch the application.
