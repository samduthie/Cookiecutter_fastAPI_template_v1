# Stage 1: Builder
FROM python:3.12-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev

# Copy source and install project
COPY . .
RUN uv sync --frozen --no-dev

# Stage 2: Runtime
FROM python:3.12-slim

WORKDIR /app

# Copy the venv AND the application code
COPY --from=builder /app /app

# Point to the venv
ENV PATH="/app/.venv/bin:$PATH"

# Use your FastAPI/Uvicorn command from before
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]