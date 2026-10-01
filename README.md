# E-Commerce Architecture Comparison: Monolith vs Microservices

This repository contains a comparative research project evaluating monolithic versus microservice architectures within an e-commerce domain. The codebase is organized as a monorepo containing distinct implementations alongside benchmarking and deployment infrastructure.

---

## Repository Structure

```text
ecommerce-architecture-comparison/
├── .github/                    # CI/CD workflows
├── monolith/                   # Monolithic application (Django, DRF)
├── microservices/              # Microservice platform (FastAPI, planned)
├── benchmarks/                 # Load testing and performance evaluation (planned)
├── .gitignore
├── .pre-commit-config.yaml     # Global pre-commit hooks configuration
├── pyproject.toml              # Global development dependencies and Ruff settings
└── README.md
```

---

## Prerequisites

Ensure you have the following tools installed on your host machine:

- **Python 3.12+**
- **Git**
- **uv** (recommended package and project manager)

To install `uv` (if not already installed):
- **Windows (PowerShell):**
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
  ```
- **macOS / Linux:**
  ```bash
  curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
  ```

---

## Initial Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/ecommerce-architecture-comparison.git
   cd ecommerce-architecture-comparison
   ```

2. **Initialize root virtual environment & install developer tools:**
   Install global code-quality tools (`ruff`, `pre-commit`) managed via `uv`:
   ```bash
   uv sync
   ```

3. **Install Git Hooks:**
   Register the pre-commit hooks into the local `.git/hooks` directory:
   ```bash
   uv run pre-commit install
   ```

---

## Code Quality & Pre-Commit Workflow

This repository enforces consistent formatting and linting standards using **Ruff** executed via **pre-commit** hooks.

### How Git Hooks Work on Commit
Whenever you stage files and execute `git commit`, the configured hooks will run automatically:
1. Validates whitespace and file integrity.
2. Checks YAML syntax.
3. Automatically fixes code formatting, linting issues, and imports order using Ruff.

If a hook modifies any files (e.g., auto-formatting quotes or reordering imports), the commit will be stopped so you can inspect the changes. Simply re-stage the updated files and commit again:
```bash
git add .
git commit -m "feat: your meaningful commit message"
```

### Manual Verification
You can manually run code quality checks across the entire repository at any time:

- **Run all pre-commit hooks:**
  ```bash
  uv run pre-commit run --all-files
  ```

- **Run Ruff linter directly:**
  ```bash
  uv run ruff check .
  ```

- **Run Ruff linter with auto-fix:**
  ```bash
  uv run ruff check . --fix
  ```

- **Run Ruff formatter:**
  ```bash
  uv run ruff format .
  ```

---

## Subproject Development

Each subsystem within this repository operates with an isolated environment to ensure clean dependencies:

- **Monolith:** Navigate to `monolith/` and follow the dedicated instructions in `monolith/README.md`.
- **Microservices:** Developed within `microservices/` using independent dependency specifications.
