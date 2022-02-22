import os

import uvicorn
from fastapi import FastAPI

from app.routers import healthcheck


app = FastAPI(
    title="{{ cookiecutter.app_name }}",
    version="{{ cookiecutter.app_version }}",
    description="{{ cookiecutter.app_description }}"
)

app.include_router(healthcheck.router)

@app.get("/")
async def root():
    """
        Load the project name as a message on the API root route.
    """
    return {"message": "{{ cookiecutter.app_name }}"}


if __name__ == "__main__":
    uvicorn.run(app, log_level="info")
