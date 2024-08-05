from fastapi import FastAPI, Request
import time
import uuid
from starlette.datastructures import MutableHeaders
from fastapi.middleware.cors import CORSMiddleware

from app.api import (
   plot_router
)


app = FastAPI(title="CHARTS-BE")


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_and_uuid_header(request: Request, call_next):
    start_time = time.time()
    request_id = uuid.uuid4().__str__()
    new_header = MutableHeaders(request.headers)
    new_header["X-Request-Id"] = request_id
    request._headers = new_header
    request.scope.update(headers=request.headers.raw)
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["X-Request-Id"] = request_id
    return response


app.include_router(plot_router)



@app.get("/")
async def root():
    return {"message": "Hello World"}
