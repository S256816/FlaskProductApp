# Flask Product Management App

## About the Project

Flask Product Management App is a standalone web application developed with Python, Flask, and SQLite. It was created as a practical micro-artifact for the In-Depth Study in the Development of Web Applications course.

The application allows users to manage product information through CRUD operations: Create, Read, Update, and Delete.

## Features

- View products stored in the database
- Add new products
- Edit existing products
- Delete products
- Validate form input
- Display success and error messages
- Confirm product deletion before submitting the form
- Store product information in an SQLite database

Each product contains the following fields:

- ID
- Name
- Description
- Price
- Category

## Technologies Used

- **Python** – application programming
- **Flask** – web framework and request routing
- **SQLite** – database for storing product information
- **HTML** – page structure and forms
- **CSS** – page styling and responsive layout
- **Jinja** – HTML templates rendered by Flask
- **JavaScript** – inline confirmation before deleting a product

## Project Structure

```text
FlaskProductApp/
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

The SQLite database file, `products.db`, is created locally when the application starts. It is not included in the GitHub repository.

## Installation and Setup

### Prerequisites

- Python
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/S256816/FlaskProductApp.git
```

### 2. Open the Project Folder

```bash
cd FlaskProductApp
```

### 3. Install Dependencies

Install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Start the application with:

```bash
python app.py
```

If your system uses `python3`, run:

```bash
python3 app.py
```

### 5. Open the Application

Open the local address displayed in the terminal. The default Flask development address is:

http://127.0.0.1:5000

## Database

The application uses SQLite to store product information.

When the application starts, it initializes the database and creates the `products` table if it does not already exist. The table contains an automatically generated ID and fields for the product name, description, price, and category.

The database file is generated locally and is not included in the GitHub repository.

## Application Structure

The application uses Flask routes in `app.py` to handle product operations and interact with the SQLite database. The `templates/index.html` file provides the user interface through HTML and Jinja templates, with CSS styling and inline JavaScript for deletion confirmation.

## Academic Context

This application was developed for the In-Depth Study in the Development of Web Applications course. It serves as a practical micro-artifact for examining Flask's architecture, routing, template rendering, form handling, database operations, and developer experience.

The accompanying report compares this Flask application with the ASP.NET Core MVC application used in Laboratory Assignment 2.

## Source Code

GitHub repository: https://github.com/S256816/FlaskProductApp
