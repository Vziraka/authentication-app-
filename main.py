# Entry point — this is the file you run to start the API server
# It creates the FastAPI app and connects the router (where your endpoints live)

from fastapi import FastAPI
from router import router

app = FastAPI(title="Simple Auth App")

app.include_router(router)
