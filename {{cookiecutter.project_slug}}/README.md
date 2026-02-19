# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Prerequisites

- Python 3.12+
- Docker and Docker Compose
- An `.env` file with the required environment variables. See `.env.example`.

## Getting Started

### Using Docker (Recommended)

This is the easiest way to get the application running.

1.  **Build and run the containers:**

    ```bash
    docker-compose up -d --build
    ```

2.  **That's it!**

    The API will be available at [http://localhost:8000](http://localhost:8000).

## Makefile Commands

A `Makefile` is provided to simplify common tasks.

*   `make build`: Build and start the services.
*   `make stop`: Stop the services.
*   `make test`: Run tests.
*   `make lint`: Lint the code.
*   `make format`: Format the code.
*   `make health`: Poll the API until it is healthy.

### Without Docker

1.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the application:**

    ```bash
    uvicorn app.main:app --reload
    ```

    The API will be available at [http://localhost:8000](http://localhost:8000).

## Database Migrations

This project uses Alembic to manage database migrations.

1.  **Create a new migration:**

    ```bash
    alembic revision --autogenerate -m "Your migration message"
    ```

2.  **Apply migrations:**

    ```bash
    alembic upgrade head
    ```
