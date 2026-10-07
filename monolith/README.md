# E-Commerce Monolith Service

Monolithic implementation of the e-commerce platform built with Django 5 and Django REST Framework. Serves as the architectural baseline for comparative performance benchmarks against microservices.

---

## Tech Stack

- **Framework:** Django 5.x, Django REST Framework
- **Database:** PostgreSQL (with SQLite fallback for lightweight local tasks)
- **Settings Management:** `django-environ`
- **Testing:** `pytest`, `pytest-django`, `pytest-cov`, `factory-boy`
- **Environment Management:** `uv`

---

## Project Structure

```text
monolith/
├── apps/               # Pluggable domain applications (products, orders, etc.)
│   └── __init__.py
├── config/             # Project settings, WSGI/ASGI, root URLs
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── .env.example        # Template for local environment variables
├── manage.py
├── pyproject.toml      # Subproject dependencies and pytest configuration
└── README.md
```

---

## Local Setup

All commands below should be executed from within the `monolith/` directory.

### 1. Install Dependencies
```bash
uv sync --dev
```

### 2. Configure Environment Variables
Create your local `.env` file from the provided template:

- **Linux / macOS:**
  ```bash
  cp .env.example .env
  ```
- **Windows (PowerShell):**
  ```powershell
  Copy-Item .env.example .env
  ```

### 3. Generate a Secure `SECRET_KEY`
To replace the placeholder key in your `.env`, generate a cryptographically strong Django secret key using the built-in management utility:

```bash
uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the generated output and update the `SECRET_KEY` variable in your `.env`:
```env
SECRET_KEY=your_generated_secret_key_here
```

### 4. Configure PostgreSQL Connection
The application uses `django-environ` to parse database connection URLs via the `DATABASE_URL` variable.

The connection string follows this standard URI format:
```text
postgres://<username>:<password>@<host>:<port>/<database_name>
```

> If `DATABASE_URL` is omitted, the application automatically falls back to a local SQLite database (`db.sqlite3`) for quick checks.

### 5. Apply Database Migrations
Make sure your PostgreSQL instance is running and the database exists, then apply migrations:
```bash
uv run python manage.py migrate
```

### 6. Verify System Integrity
```bash
uv run python manage.py check
```

### 7. Run Development Server
```bash
uv run python manage.py runserver
```

### 8. API Documentation
Once the development server is running, you can explore and test the available API endpoints using the auto-generated OpenAPI documentation:

- **Swagger UI:** [http://127.0.0.1:8000/api/docs/swagger/](http://127.0.0.1:8000/api/docs/swagger/) (Recommended for interactive testing)
- **Redoc:** [http://127.0.0.1:8000/api/docs/redoc/](http://127.0.0.1:8000/api/docs/redoc/) (Detailed, read-only reference)
- **OpenAPI Schema:** [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/) (Raw JSON/YAML schema)

---

## Development Guidelines

### Creating New Apps
All domain applications must be placed inside the `apps/` directory:
```bash
uv run python manage.py startapp <app_name> apps/<app_name>
```
*Note: Ensure the `name` attribute in `apps/<app_name>/apps.py` matches the module path (e.g., `name = "users"`).*

---

## Testing Conventions

We follow a strict **layered testing methodology** using `pytest`:

- **Layer Separation:** Keep test modules split by architectural layers (`test_models.py`, `test_serializers.py`, `test_views.py`) inside each app's `tests/` directory.
- **Class-Based Grouping:** Group test cases logically inside test classes (e.g., `class TestUserModel:`).
- **Factories (`factory-boy`):** Use `UserFactory.build()` for lightweight in-memory validation checks, and `UserFactory()` for database-dependent persistence tests.
- **Fixtures:** Define reusable test data payloads and setups using `pytest` fixtures within test modules or `conftest.py`.

### Running Tests
Execute the full test suite with code coverage:
```bash
uv run pytest
```

Run tests for a specific domain app:
```bash
uv run pytest apps/users/
```

Run a specific test class:
```bash
uv run pytest apps/users/tests/test_models.py::TestUserModel
```
