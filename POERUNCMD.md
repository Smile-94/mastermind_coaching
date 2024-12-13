# POE Commands Documentation

This documentation provides instructions for using the predefined poe commands in your project. Each command is defined in the pyproject.toml file under [tool.poe.tasks], allowing you to quickly perform essential Django tasks.

## Prerequisites

Ensure you have poethepoet installed in your environment. You can install it via poetry:

```zsh
    poetry add poethepoet
```

### Install Poe the Poet as a poetry plugin

It’ll then be available as the poetry poe command anywhere in your system.

```zsh
    poetry self add 'poethepoet[poetry_plugin]'
```

### Install Poe the Poet into your poetry project

```zsh
    poetry add --group dev poethepoet
```

## 1. Available Commands

Start the Django development server on 0.0.0.0:8000. the main command is `python manage.py runserver 0.0.0 `. Now you can run only

```zsh
    poetry run poe dev
```

Runs python manage.py runserver 0.0.0.0:8000, allowing access to the development server from any IP address.

## 2. Make Migrations

Generate new migrations based on model changes.the main command is `python manage.py makemigrations`.

```zsh
    poetry run poe migrations
```

Runs python manage.py makemigrations, which will create migration files for any changes detected in your models.

## 3. Apply Migrations

Apply migrations to the database.

```zsh
    poetry run poe migrate
```

Runs python manage.py migrate, applying all pending migrations to the database.

## 4. Create a New Django Application

Create a new Django app by providing the app name as an argument. for example: `poetry run poe app myapp`

```zsh
    poetry run poe app <app_name>
```

Runs python manage.py startapp <app_name>, creating the necessary directory structure and files for a new Django application.

Note: Replace <app_name> with the desired name for your new app.
