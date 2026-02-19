import logging
from contextlib import asynccontextmanager
from logging.config import dictConfig

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pythonjsonlogger import jsonlogger

from app.api import health
from app.core.config import settings


# Structured JSON logging
class JsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(JsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record["levelname"] = record.levelname
        log_record["name"] = record.name


log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": JsonFormatter,
            "format": "%(asctime)s %(name)s %(levelname)s %(message)s",
        },
    },
    "handlers": {
        "json": {
            "class": "logging.StreamHandler",
            "formatter": "json",
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["json"], "level": "INFO"},
        "fastapi": {"handlers": ["json"], "level": "INFO"},
        "app": {"handlers": ["json"], "level": "INFO", "propagate": False},
    },
}

dictConfig(log_config)
logger = logging.getLogger("app")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup")
    yield
    logger.info("Application shutdown")


app = FastAPI(
    title=settings.APP_NAME,
    description="A production-ready FastAPI boilerplate.",
    version="0.1.0",
    lifespan=lifespan,
)


# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred."},
    )


# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API Routers
app.include_router(health.router, prefix="/api", tags=["Health"])


@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}"}
