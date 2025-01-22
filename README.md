Project Name: Content Management System (CMS)
Overview
This project is a Content Management System (CMS) that allows authenticated users with the "author" role to create, edit, view, and delete their own content. Additionally, the "admin" role has broader privileges, allowing them to manage all users and all content.

Features
User Management: Admin can view all users, edit user details, and delete users.
Content Management: Authors can create, view, edit, and delete their own content, while admins can manage all content.
Content Search: Content can be searched by title, body, summary, and categories.
Permissions: Custom permissions ensure only authorized users can perform certain actions.
Tech Stack
Django: Python web framework for backend
Django REST Framework: For building REST APIs
PostgreSQL: For database management
Docker (Optional): For containerization
Setup
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/cms_project.git
cd cms_project
2. Install Dependencies
Create a virtual environment and install the necessary dependencies.

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
3. Setup Database
bash
Copy
Edit
# Apply migrations
python manage.py migrate

# Create a superuser (admin) for testing
python manage.py createsuperuser
4. Run the Development Server
bash
Copy
Edit
python manage.py runserver
The app will be available at http://127.0.0.1:8000/.

API Endpoints
1. User Management
View All Users (Admin Only)
URL: /api/users/
Method: GET
Permission: Admin only
Response:
json
Copy
Edit
[
  {
    "id": 1,
    "email": "admin@example.com",
    "full_name": "Admin User",
    "role": "admin",
    "phone": "1234567890",
    "pincode": "12345",
    "is_staff": true,
    "is_superuser": true
  },
  {
    "id": 2,
    "email": "author@example.com",
    "full_name": "Author User",
    "role": "author",
    "phone": "0987654321",
    "pincode": "67890",
    "is_staff": false,
    "is_superuser": false
  }
]
Edit User (Admin Only)
URL: /api/users/{id}/

Method: PUT

Permission: Admin only

Request Body:

json
Copy
Edit
{
  "full_name": "Updated Name",
  "role": "author",
  "phone": "1231231234"
}
Response:

json
Copy
Edit
{
  "id": 2,
  "email": "author@example.com",
  "full_name": "Updated Name",
  "role": "author",
  "phone": "1231231234",
  "pincode": "67890",
  "is_staff": false,
  "is_superuser": false
}
Delete User (Admin Only)
URL: /api/users/{id}/
Method: DELETE
Permission: Admin only
Response: 204 No Content
2. Content Management
Create Content (Authenticated Authors Only)
URL: /api/content/

Method: POST

Permission: Author only

Request Body:

json
Copy
Edit
{
  "title": "Sample Title",
  "body": "This is the body of the content.",
  "categories": [1, 2]
}
Response:

json
Copy
Edit
{
  "id": 1,
  "title": "Sample Title",
  "body": "This is the body of the content.",
  "categories": [
    {
      "id": 1,
      "name": "Category 1"
    },
    {
      "id": 2,
      "name": "Category 2"
    }
  ],
  "author": 1
}
Get All Content (Admin Sees All, Author Sees Their Own)
URL: /api/content/
Method: GET
Permission: Admin can see all; author can only see their own content
Response:
json
Copy
Edit
[
  {
    "id": 1,
    "title": "Sample Title",
    "body": "This is the body of the content.",
    "categories": [
      {
        "id": 1,
        "name": "Category 1"
      }
    ]
  }
]
Search Content (Filter by Title, Body, Summary, and Categories)
URL: /api/content/search/?query=term
Method: GET
Response:
json
Copy
Edit
[
  {
    "id": 1,
    "title": "Sample Title",
    "body": "This is the body of the content.",
    "categories": [
      {
        "id": 1,
        "name": "Category 1"
      }
    ]
  }
]
Edit Content (Authenticated Author or Admin Only)
URL: /api/content/{id}/

Method: PUT

Permission: Author edits their own content, admin can edit any content

Request Body:

json
Copy
Edit
{
  "title": "Updated Title",
  "body": "Updated body content."
}
Response:

json
Copy
Edit
{
  "id": 1,
  "title": "Updated Title",
  "body": "Updated body content.",
  "categories": [
    {
      "id": 1,
      "name": "Category 1"
    }
  ],
  "author": 1
}
Delete Content (Authenticated Author or Admin Only)
URL: /api/content/{id}/
Method: DELETE
Permission: Author can delete their own content, admin can delete any content
Response: 204 No Content
Permissions and Roles
Admin: Can view all users, edit users, delete users, and manage all content.
Author: Can create, edit, view, and delete their own content.
Running Tests
To run tests for the API:

bash
Copy
Edit
python manage.py test