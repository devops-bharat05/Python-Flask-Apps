## URL Shortener Web Application

A simple URL shortener web application built with Flask. This app allows users to enter long URLs and obtain shorter versions. Each short URL redirects users to the original URL when accessed.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)

## Project Overview

This project provides a straightforward solution for shortening URLs, inspired by services like Bitly or TinyURL. Users can enter a long URL, receive a shortened version, and share it. Whenever the shortened URL is accessed, the user is redirected to the original link.

## Features

- **URL Shortening**: Enter a long URL and get a shortened version.
- **Redirects**: Accessing the short URL redirects to the original URL.
- **Unique Short IDs**: Each URL is associated with a unique short ID.
- **SQLite Database Integration**: Stores original URLs and short IDs persistently.

## Project Structure

```
url_shortener/
├── app.py               # Main Flask application file
├── config.py            # Configuration file for Flask and database
├── models.py            # Database model definitions
├── requirements.txt     # List of dependencies
└── templates/           # HTML templates
    ├── home.html        # Form for URL input
    └── result.html      # Display of the shortened URL
```

## Installation

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/url_shortener.git
   cd url_shortener
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The app’s configuration is stored in `config.py`. You can modify the following variables:

- **`SQLALCHEMY_DATABASE_URI`**: Sets the SQLite database file.
- **`SECRET_KEY`**: A secret key for Flask session management. Replace with a strong, unique key.

Example configuration in `config.py`:

```python
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'urls.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'your_secret_key'
```

## Usage

1. **Initialize the Database**
   Run this command in the project directory to create the SQLite database:
   ```python
   python app.py
   ```
   This will create the `urls.db` file, storing the original URLs and their shortened versions.

2. **Start the Flask Application**
   ```bash
   python app.py
   ```
   By default, the app runs on `http://127.0.0.1:5000/`.

3. **Access the Application**

   Open your browser and go to `http://127.0.0.1:5000/` to use the URL shortener.

4. **Shorten a URL**
   - Enter a long URL in the form and submit.
   - You’ll receive a shortened URL which you can copy and share.

5. **Redirect Using Short URL**
   - Open the shortened URL in a new tab, and it will redirect you to the original URL.

## Technologies Used

- **Flask**: Web framework for Python to handle HTTP requests and routing.
- **Flask-SQLAlchemy**: ORM (Object Relational Mapper) for database management with SQLite.
- **SQLite**: Lightweight database used for storing URLs and short IDs.

## Future Enhancements

- **Custom Short IDs**: Allow users to define their custom short ID if available.
- **Analytics**: Track how many times each shortened URL has been accessed.
- **User Authentication**: Enable users to log in and manage their shortened URLs.
- **Link Expiration**: Set expiration dates for short URLs.
- **API Endpoints**: Provide API endpoints for programmatic access to URL shortening.

---

### Example Usage

1. Start the Flask app:
   ```bash
   python app.py
   ```
2. Go to `http://127.0.0.1:5000/`.
3. Enter the URL to shorten and submit. You will receive a shortened URL in the format `http://127.0.0.1:5000/<short_id>`.
4. Accessing this shortened URL will redirect to the original URL.

---

This URL shortener app is designed for educational purposes and as a starter template for learning Flask. Feel free to customize and expand it as needed for more advanced features!
