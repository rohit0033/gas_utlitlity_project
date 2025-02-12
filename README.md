# Gas Utility Project

This project is a Django-based web application for managing customer service requests for a gas utility company. It allows customers to submit and track service requests, and provides tools for support representatives to manage these requests efficiently.

## Table of Contents

1.  [Introduction](#introduction)
2.  [Prerequisites](#prerequisites)
3.  [Installation](#installation)
4.  [Configuration](#configuration)
5.  [Running the Application](#running-the-application)
6.  [Creating a Superuser](#creating-a-superuser)
7.  [Running Tests](#running-tests)
8.  [API Endpoints](#api-endpoints)
9.  [Project Structure](#project-structure)
10. [Contributing](#contributing)
11. [License](#license)

## 1. Introduction

This application aims to streamline customer service operations for a gas utility company by providing a self-service portal for customers and efficient management tools for support representatives.

## 2. Prerequisites

Before you begin, ensure you have the following installed:

*   Python (version 3.8 or higher)
*   pip (Python package installer)
*   Git

## 3. Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd gas_utility_project
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   On Windows:

        ```bash
        venv\Scripts\activate
        ```

    *   On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## 4. Configuration

1.  **Database settings:**

    The project uses SQLite by default. You can configure the database settings in [settings.py](http://_vscodecontentref_/0). If you want to use another database (e.g., PostgreSQL), update the [DATABASES](http://_vscodecontentref_/1) setting accordingly.

2.  **Other settings:**

    Review the other settings in [settings.py](http://_vscodecontentref_/2) and adjust them as needed for your environment (e.g., [SECRET_KEY](http://_vscodecontentref_/3), [DEBUG](http://_vscodecontentref_/4), [ALLOWED_HOSTS](http://_vscodecontentref_/5)).

## 5. Running the Application

1.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

2.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at [http://127.0.0.1:8000/](http://_vscodecontentref_/6).

## 6. Creating a Superuser

To access the Django admin panel, you need to create a superuser:

```bash
python manage.py createsuperuser

7. Running Tests
To run the project's tests:

8. API Endpoints
Here are some of the available API endpoints:

POST /api/accounts/register/ - Register a new user
POST /api/accounts/login/ - Log in an existing user
POST /api/accounts/logout/ - Log out the current user
POST /api/service-requests/create/ - Create a new service request
GET /api/service-requests/list/ - List all service requests for the logged-in user
GET /api/service-requests/<id>/ - Get details of a specific service request
POST /api/support/requests/<id>/update_status/ - Update the status of a service request (support representatives only



project_root/
    |-- config/                   # Configuration settings
    |-- accounts/             # User authentication & management
    |-- service_requests/     # Service request handling
    |-- support/              # Support representative tools
    |-- templates/               # HTML templates (if applicable)
    |-- static/                  # Static files (CSS, JS, Images)
    |-- media/                   # User-uploaded files
    |-- requirements.txt          # Dependencies
    |-- manage.py                 # Django management script
