from fastapi import FastAPI
from prometheus_client import Summary
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)

REQUEST_RESPOND_TIME = Summary('app_response_latency_seconds', 'Response latency in seconds')

@app.get("/")
#@REQUEST_RESPOND_TIME.time()
async def root():
    return {"message": "Hello World"}