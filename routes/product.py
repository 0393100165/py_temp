from fastapi import APIRouter, Request
from models.products import Product
from config.database import products_collection
from schema.products import list_serial
from bson import ObjectId

routes_product = APIRouter()

@routes_product.get("/products")
async def get_products():
    products = list_serial(products_collection.find())
    return products