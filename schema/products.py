def individual_serial(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product.get("name", ""),
        "description": product.get("description", "")
    }

def list_serial(products) -> list:
    return[individual_serial(product) for product in products]