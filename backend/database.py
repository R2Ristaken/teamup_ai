from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import AsyncGenerator
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # Fallback for development/testing if no env var is set
    # In production, this should fail or reference a real DB
    print("WARNING: DATABASE_URL not set, using sqlite fallback for now")
    DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Create Async Engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True, # Set to False in production
)

# Create Session Factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for getting async database sessions"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
