from typing import AsyncGenerator

import redis.asyncio as redis
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import settings

# Create the async engine
async_engine = create_async_engine(
    settings.database_uri_async,
    pool_pre_ping=True,
    echo=False,  # Set to True to see SQL queries
)

# Create a sessionmaker
AsyncSessionFactory = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    autoflush=False,
)

# Redis connection pool
redis_pool = redis.ConnectionPool.from_url(
    f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    max_connections=10,
    encoding="utf-8",
    decode_responses=True,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to get an async database session.
    """
    async with AsyncSessionFactory() as session:
        yield session


async def get_redis() -> redis.Redis:
    """
    Dependency to get a Redis connection.
    """
    return redis.Redis(connection_pool=redis_pool)
