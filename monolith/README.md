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

---

## Running Tests

Execute the full test suite with code coverage:

```bash
uv run pytest
```
