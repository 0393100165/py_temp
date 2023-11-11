from fastapi import APIRouter, Request
from models.agents import Agent
from config.database import colection_name
from schema.schemas import list_serial
from bson import ObjectId

routes_agent = APIRouter()

@routes_agent.get("/")
async def get_agents():
    agents = list_serial(colection_name.find())
    return agents

@routes_agent.post("/")
async def post_agent(agent: Agent):
    colection_name.insert_one(dict(agent))