# FastAPI Media Library API

**Individual School Project**
This project was carried out as an individual assignment during my computer science studies at Ynov Campus. I designed and developed it individually to validate my backend development skills using Python.

## Description
This is a media library management REST API developed with FastAPI and SQLite. It allows the creation, consultation, modification, and deletion of musical albums (full CRUD). The API includes a JWT token authentication system to secure modification routes, as well as interactive Swagger documentation.

## Tech Stack
- **Python 3.9+**: Main programming language.
- **FastAPI**: Modern and fast backend framework.
- **Uvicorn**: ASGI server for FastAPI.
- **SQLite**: Lightweight local database (`albums.db`).
- **Pydantic**: Data validation and strong typing.
- **Pytest**: Automated testing framework.

## Installation Prerequisites
- Python 3.9 or higher.
- Pip (Python package manager).

## Installation and Launch
To install and run the project locally, follow these commands (in PowerShell):

1. Create and activate a virtual environment, then install the dependencies:
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

2. Start the development server:
```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

The API will start at http://127.0.0.1:8000. 
The Swagger testing interface is available at http://127.0.0.1:8000/docs.

## Demo Account
The API includes a default user for testing secure routes via Swagger (**Authorize** button):
- Username: `admin`
- Password: `Albums2026!`
(The token expires after 30 minutes).

## Tests
To run automated tests:
```powershell
.\.venv\Scripts\python.exe -m pytest
```

## Project Structure
```
projet_final_python_FastAPI/
├── app/               # FastAPI source code
│   ├── main.py        # Application entry point
│   ├── models.py      # Pydantic models for validation
│   ├── routes.py      # API endpoints definition
│   ├── security.py    # Authentication and JWT logic
│   └── database.py    # SQLite connection management
├── tests/             # Folder containing Pytest tests
├── albums.db          # Persistent SQLite database
├── requirements.txt   # List of Python dependencies
└── README.md          # Project documentation
```
