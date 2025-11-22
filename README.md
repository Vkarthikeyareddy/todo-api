# todo-api
📌 Todo API – FastAPI + HTML/JS
A full-stack Todo application built with FastAPI, Python, and a lightweight HTML/JavaScript frontend.
Includes complete REST API, business logic module, unit tests, API tests, and CI automation.

🚀 Features

🗄 Backend (FastAPI)
Create, list, delete, and complete todos
Separate business logic (todo.py) and API routes (api.py)
Pydantic request/response models
CORS enabled for browser-based frontend
Auto-generated Swagger UI & ReDoc documentation

🎨 Frontend (HTML + JS)
Pure HTML/JavaScript UI (no frameworks needed)
Add todos
Mark as completed
Delete todos
Live UI updates using Fetch API

🧪 Testing
Unit tests for core logic
API tests using FastAPI TestClient
Complete test coverage for CRUD flows

🔄 CI Pipeline
GitHub Actions workflow running pytest on every push & PR

📂 Project Structure
todo-api/
│
├── todo_api/
│   ├── api.py           # FastAPI routes
│   ├── todo.py          # Business logic
│   └── __init__.py
│
├── frontend/
│   └── index.html       # UI
│
├── tests/
│   ├── test_todo.py     # Unit tests
│   └── test_api.py      # API tests
│
├── .github/workflows/
│   └── ci.yml           # GitHub Actions pipeline
│
├── main.py              # App entrypoint (uvicorn)
├── requirements.txt
└── README.md

🛠 Installation
git clone https://github.com/yourusername/todo-api.git
cd todo-api
pip install -r requirements.txt

▶ Running the Backend
uvicorn main:app --reload
Backend runs at:
http://127.0.0.1:8000
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

💻 Running the Frontend
Serve the frontend with a simple HTTP server:
cd frontend
python -m http.server 5500
Then open:
👉 http://localhost:5500/index.html

🧪 Running Tests
pytest

📡 API Endpoints
Method	Endpoint	Description
GET	/todos	List all todos
POST	/todos	Create a new todo
DELETE	/todos/{id}	Delete todo
POST	/todos/{id}/complete	Mark todo as completed
GET	/todos/pending	List pending todos
GET	/todos/completed	List completed todos

🏗 Built With
FastAPI
Python
Pydantic
HTML / JavaScript
Pytest
GitHub Actions

📈 Future Enhancements
Add SQLite/PostgreSQL database
Add authentication (JWT)
Add update/edit endpoint
Convert UI into a React SPA
Dockerize app for deployment

👤 Author
Karthikeya Reddy Vanguru