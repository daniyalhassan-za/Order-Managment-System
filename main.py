from  fastapi import FastAPI
from model import OrderModel

app = FastAPI()

@app.post("/order/")
async def create_order(order : OrderModel ):
    return{"message" : f"Order Succesfully {order}"}

@app.get("/order/{order_id}")
async def track_order(order_id: int):
    return {"message" : f"Track Your order by {order_id}"}
