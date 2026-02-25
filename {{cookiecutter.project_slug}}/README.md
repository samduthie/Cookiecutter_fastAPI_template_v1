# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Prerequisites

- Python 3.12+
- Docker and Docker Compose
- An `.env` file with the required environment variables. See `.env.example`.
- A `.env` file with your local environment variables. You can copy the `.env.example` file to get started (`cp .env.example .env`).

## Getting Started

### Using Docker (Recommended)

This is the easiest way to get the application running.

1.  **Build and run the containers:**

    ```bash
    docker-compose up -d --build
    ```

2.  **That's it!**

    The API will be available at http://localhost:{{ cookiecutter.app_port }}.

    > **Note for Linux Users:** Docker mounts the current directory by default. Files created inside the container (like `__pycache__`) may be owned by `root`. To avoid permission issues, you can run the container with your user ID:
    >
    > `CURRENT_UID=$(id -u):$(id -g) docker-compose up -d --build`

## Development

A `Makefile` is provided to simplify common tasks.

*   `make build`: Build and start the services using Docker Compose.
*   `make stop`: Stop the services.
*   `make test`: Run the test suite using `pytest` inside the Docker container.
*   `make lint`: Lint the code with `ruff`.
*   `make format`: Format the code with `ruff`.
*   `make health`: Poll the API's health check endpoint until it is healthy.

### Database Migrations

This project uses Alembic to manage database migrations. Migrations are automatically applied when the application starts up with Docker Compose.

To create a new migration based on model changes, run the following command:

```bash
docker-compose exec api alembic revision --autogenerate -m "Your migration message"
```

This will generate a new migration script in the `alembic/versions` directory.

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
    The API will be available at [http://localhost:{{ cookiecutter.app_port }}](http://localhost:{{ cookiecutter.app_port }}).
