from pydantic import BaseModel

class Agent(BaseModel):
    name: str
    email: str