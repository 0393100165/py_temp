from fastapi import FastAPI
from routes.agent import routes_agent

app = FastAPI()

app.include_router(routes_agent)
