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

- **Programming Languages**: Python, C++
- **Database Management Systems**: MariaDB
- **Other Tools**: Wearable to collect patient data

## Prerequisites

- Windows computer
- Python 3.x
- MariaDB
- Kali Linux in VirtualBox
- Arduino IDE
- Visual Studio IDE

## Step 1: Setup Development Environment

### Install Python
1. Download the latest version of Python from the [official website](https://www.python.org/downloads/).
2. Run the installer and follow the on-screen instructions to complete the installation.
3. Verify the installation by opening a command prompt and typing:
    ```sh
    python --version
    ```

### Install MariaDB
1. Download MariaDB from the [official website](https://mariadb.org/download/).
2. Run the installer and follow the on-screen instructions to install MariaDB.
3. Configure MariaDB and create a database for Health Shield:
    ```sql
    CREATE DATABASE health_shield_db;
    ```

### Install VirtualBox and Setup Kali Linux
1. Download VirtualBox from the [official website](https://www.virtualbox.org/wiki/Downloads).
2. Install VirtualBox by running the downloaded file and following the on-screen instructions.
3. Download Kali Linux from the [official website](https://www.kali.org/get-kali/#kali-virtual-machines).
4. Import the Kali Linux VM into VirtualBox and start it.

### Install Arduino IDE
1. Download the Arduino IDE from the [official website](https://www.arduino.cc/en/software).
2. Run the installer and follow the on-screen instructions to complete the installation.

### Install Visual Studio IDE
1. Download Visual Studio from the [official website](https://visualstudio.microsoft.com/downloads/).
2. Run the installer and follow the on-screen instructions to complete the installation.

## Step 2: Clone the Repository

Clone the Health Shield repository from GitHub:
```sh
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

sh
Copy code
pip install -r requirements.txt
Step 5: Configure the Application
Create a .env file in the root directory of the project and add the following configurations:
env
Copy code
DATABASE_URI=mysql+pymysql://username:password@localhost/health_shield_db
Replace username and password with your MariaDB credentials.
Step 6: Initialize the Database
Run the following commands to create the necessary tables in the database:

sh
Copy code
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
Step 7: Running the Application
Start the Python application:

sh
Copy code
python app.py
The application will be available at http://127.0.0.1:5000.

Deliverables
The Health Shield prototype.
Detailed documentation to guide users and developers through the setup and usage of Health Shield.
References
Python Documentation
MariaDB Documentation
GNS3 Documentation
VirtualBox Documentation
Kali Linux Documentation
Arduino IDE Documentation
Visual Studio Documentation
About
An anonymization tool for health records designed to promote trust and confidentiality in healthcare environments while facilitating data-driven decision-making and analysis.

Languages Used
C++ 47.2%
Python 37.6%
HTML 10.0%
CSS 5.2%
