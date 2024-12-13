# Django Project Setup with Poetry

This guide provides steps to set up and run a Django project using [Poetry](https://python-poetry.org/), a dependency management and packaging tool for Python.

## Prerequisites

- **Python** (version >= 3.12)
- **Poetry** (version >= 1.8.0)
  - Install Poetry by running:
    ```zsh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

## Getting Started

1. **Clone the Repository**

   Clone the repository to your local machine:

   ```zsh
   git clone https://github.com/Smile-94/django-template.git
   cd to django-template
   ```

## Install Dependencies

Use Poetry to install project dependencies specified in `pyproject.toml`:

```zsh
   poetry install
```

## Set Up Environment Variables

Create a `.env` file in the root of your project to store environment variables. For example:

```zsh
PROJECT_ENVIRONMENT='local'
```

Now Create a env directory and inside the env directory create a a `.env` file by specifying your environment variable like `.env.local`. Environment variables example are given in the env.dist file.

## Apply Migrations

Run database migrations to set up your database schema:

```zsh
   poetry run python manage.py migrate

```

## Run the Development Server

Start the Django development server:

```zsh
   poetry python manage.py runserver 0.0.0.0:8000
```
