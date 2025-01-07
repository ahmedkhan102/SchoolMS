School Management System with AI

This project is a comprehensive School Management System integrated with Artificial Intelligence to enhance administrative tasks and improve user experience. It offers features such as automated attendance, student and teacher management, fee tracking, and AI-driven analytics.

Features AI-Powered Attendance: Facial recognition for automated attendance tracking. Student Management: Add, edit, and manage student details. Teacher Scheduling: Manage teacher schedules efficiently. Fee Management: Track student fee records and generate invoices. Data Analytics: Gain insights using AI-driven data analysis. Role-Based Access Control: Separate dashboards for admins, teachers, and students.

Folder Structure

SchoolManagementSystem/
├── mainapp.py               # Main entry point for the application
├── setup.py                 # Setup script for project dependencies
├── requirements.txt         # Python dependencies
├── _secret_auth.json        # Authentication details (sample file)
├── README.md                # Project documentation
├── streamlit_login_auth_ui/ # Streamlit-based UI for login and authentication
├── tests/                   # Contains test scripts
├── src/                     # Core application code
│   ├── routes/              # API routes for different user roles
│   ├── ai_module/           # AI features like facial recognition
│   └── database/            # Database models and utilities
Setup and Installation

Prerequisites Python 3.8 or higher Virtual environment tool (e.g., venv or conda)

Steps

Clone the repository:

git clone https://github.com/yourusername/SchoolManagementSystem.git
cd SchoolManagementSystem
Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install the dependencies:

pip install -r requirements.txt
Run the application:

python mainapp.py
Open the application in your browser at http://localhost:5000.

Usage

Launch the app by running mainapp.py.
Access role-specific dashboards (Admin, Teacher, or Student) using the provided credentials.
Testing To run all the test cases:

pytest tests/
Contributing Contributions are welcome! Follow these steps to contribute:

Fork the repository.
Create a new feature branch.
Commit your changes and push to the branch.
Submit a pull request.
