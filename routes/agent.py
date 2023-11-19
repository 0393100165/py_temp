from fastapi import APIRouter, Request
from models.agents import Agent
from config.database import agents_collection
from schema.agents import list_serial
from bson import ObjectId

routes_agent = APIRouter()

@routes_agent.get("/agents")
async def get_agents():
    agents = list_serial(agents_collection.find())
    return agents

@routes_agent.post("/create")
async def post_agent(agent: Agent):
    agents_collection.insert_one(dict(agent))