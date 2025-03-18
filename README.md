# Task Manager API

Task Manager API is a Django REST framework-based application that allows users to manage their tasks efficiently. It provides features like task creation, filtering, pagination, and custom permissions.

## Features
- Create, update, delete, and list tasks
- Task filtering by completion status and date ranges
- Pagination for task listings
- Admin-only access to all tasks
- Token-based authentication using Django REST Framework JWT
- Error handling for bad requests and missing authentication

---
## Installation and Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.11+
- Django 5+
- PostgreSQL (or SQLite for development)
- Docker (optional, for containerization)
- Git
- Postman (optional, for testing API endpoints)

### Step 1: Clone the Repository
```sh
 git clone https://github.com/Jotsna22/taskmanager.git
 cd taskmanager
```

### Step 2: Create a Virtual Environment
```sh
 python -m venv venv
 source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```sh
 pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file in the root directory and set up necessary variables:
```sh
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  # Change for PostgreSQL in production
```

### Step 5: Run Database Migrations
```sh
 python manage.py migrate
```

### Step 6: Create a Superuser (for Admin Access)
```sh
 python manage.py createsuperuser
```

### Step 7: Start the Server
```sh
 python manage.py runserver
```
Server will start at: `http://127.0.0.1:8000/`

---
## API Endpoints

| Method | Endpoint | Description |
|--------|-------------|-------------|
| POST   | `/api/token/` | Get access and refresh tokens |
| GET    | `/api/tasks/` | List tasks (pagination enabled) |
| POST   | `/api/tasks/` | Create a task |
| PUT    | `/api/tasks/{id}/` | Update a task |
| DELETE | `/api/tasks/{id}/` | Delete a task |

### Authentication
Use the `Authorization: Bearer <access_token>` header for authenticated requests.

---
## Running with Docker (Optional)

### Step 1: Build and Run the Container
```sh
docker-compose up --build
```
This will start the Django API on port `8000`.

---
## Running Tests
To run unit tests, use:
```sh
python manage.py test
```

---
## Contributing
Feel free to fork the repository and submit a pull request with improvements!

---
## License
MIT License

