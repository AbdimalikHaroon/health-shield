
# Health Shield

## Overview
Health Shield is a dedicated solution designed to safeguard sensitive health data in IoT-enabled healthcare settings. With the proliferation of Internet of Things (IoT) devices collecting vast amounts of health data, protecting patient privacy and confidentiality has become a top priority. Health Shield addresses this challenge by providing an approach to data anonymization, ensuring that health records remain secure during transmission and analysis.

## Objectives
- Ensure the security and confidentiality of health data in IoT-enabled healthcare settings.
- Implement advanced anonymization techniques to protect patient privacy.
- Facilitate secure data transmission and storage.
- Provide a user-friendly interface for data analysis and decision-making.

## Methodology
The development of Health Shield follows agile development practices, specifically Scrum, to iteratively design, develop, and prototype the solution. The following tools and technologies are used:

- **Programming Languages**: Python
- **Frameworks**: Flask
- **Database Management Systems**: MySQL
- **Other Tools**: Wearable to collect patients data

## Prerequisites
- Windows computer
- Python 3.x
- MySQL
- C++
-Wearable 

## Step 1: Setup Development Environment

### Install Python
1. Download the latest version of Python from the [official website](https://www.python.org/downloads/).
2. Run the installer and follow the on-screen instructions to complete the installation.
3. Verify the installation by opening a command prompt and typing:
   ```sh
   python --version
Install MySQL
Download MySQL from the official website.
Run the installer and follow the on-screen instructions to install MySQL.
Configure MySQL and create a database for Health Shield:
sql

CREATE DATABASE health_shield_db;
Step 2: Clone the Repository
Clone the Health Shield repository from GitHub:

git clone https://github.com/yourusername/health-shield.git
cd health-shield
Step 3: Setup Virtual Environment
Create and activate a virtual environment:

sh
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Step 4: Install Dependencies
Install the required Python packages:

pip install -r requirements.txt
Step 5: Configure the Application
Create a .env file in the root directory of the project and add the following configurations:
env

FLASK_APP=app
FLASK_ENV=development
DATABASE_URI=mysql+pymysql://username:password@localhost/health_shield_db
Replace username and password with your MySQL credentials.
Step 6: Initialize the Database
Run the following commands to create the necessary tables in the database:

flask db init
flask db migrate
flask db upgrade
Step 7: Running the Application
Start the Flask development server:

flask run
The application will be available at http://127.0.0.1:5000.

The Health Shield prototype.
Detailed documentation to guide users and developers through the setup and usage of Health Shield.
