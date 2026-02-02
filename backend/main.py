from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from worker_config import create_worker_pool
from arq import ArqRedis

# Global to hold the pool configuration
# In a real app, use request.app.state.arq_pool
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting up... Connecting to Redis/Arq")
    app.state.arq_pool = await create_worker_pool()
    yield
    # Shutdown
    print("Shutting down... Closing Redis connection")
    await app.state.arq_pool.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World", "Status": "Redis Worker Connected"}

@app.post("/test-task")
async def trigger_task(message: str = "Hello from API"):
    """
    Enqueue a background job to process a message.
    """
    redis: ArqRedis = app.state.arq_pool
    # Enqueue the job 'process_whatsapp_message' defined in worker.py
    job = await redis.enqueue_job('process_whatsapp_message', {'from': 'api-test', 'body': message})
    return {"job_id": job.job_id, "status": "queued"}
