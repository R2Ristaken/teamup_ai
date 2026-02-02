from arq import create_pool
from arq.connections import RedisSettings
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
# Parse redis URL simpler for example or use a library, 
# here assuming a standard connection string for simplicity 
# or letting arq handle defaults if just hostname provided.
# Arq RedisSettings matches standard redis-py args usually.

async def get_redis_settings():
    """
    Parses the REDIS_URL and returns arq RedisSettings.
    Handles 'redis://host:port' format basic parsing.
    """
    if "://" in REDIS_URL:
        # Very basic parsing, for production use a robust parser
        # ex: redis://:pass@localhost:6379/0
        from urllib.parse import urlparse
        r = urlparse(REDIS_URL)
        return RedisSettings(
            host=r.hostname,
            port=r.port or 6379,
            password=r.password,
            database=0 # Default to db 0
        )
    return RedisSettings(host="localhost", port=6379)

async def create_worker_pool():
    settings = await get_redis_settings()
    return await create_pool(settings)
