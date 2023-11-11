def individual_serial(agent) -> dict:
    return {
        "id": str(agent["_id"]),
        "name": agent["name"],
        "email": agent["email"]
    }

def list_serial(agents) -> list:
    return[individual_serial(agent) for agent in agents]