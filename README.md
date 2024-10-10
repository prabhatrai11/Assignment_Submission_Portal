Assignment Submission Portal
A backend system built using Django and Django REST Framework for managing assignment submissions. This system allows users to upload assignments and admins to review and manage these submissions by accepting or rejecting them. The system uses MongoDB as the database for storing assignments and user/admin data.

Features:
User Functionality:
Register and log in as a user.
Upload assignments with details including the task, admin name, and user ID.
Admin Functionality:
Register and log in as an admin.
View all assignments tagged to the admin.
Accept or reject submitted assignments.
Endpoints:
User Endpoints:

POST /register - Register a new user.
POST /login - User login.
POST /upload - Upload an assignment.
GET /admins - Get a list of all admins.
Admin Endpoints:

POST /register - Register a new admin.
POST /login - Admin login.
GET /assignments - View assignments tagged to the admin.
POST /assignments/:id/accept - Accept an assignment.
POST /assignments/:id/reject - Reject an assignment.
Tech Stack:
Backend Framework: Django, Django REST Framework
Database: MongoDB
Authentication: Django authentication system (Optional: OAuth2)
Python Version: 3.x
Setup Instructions:
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/assignment-submission-portal.git
cd assignment-submission-portal
Create a virtual environment and install dependencies:

bash
Copy code
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
pip install -r requirements.txt
Set up the database connection in settings.py.

Run migrations:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
