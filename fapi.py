# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/data")
# async def get_data():
#     return {"message": "Hello from FastAPI!"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

# from fastapi import FastAPI
# import random

# app = FastAPI()

# names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah"]

# @app.get("/random_name")
# async def get_random_name():
#     return {"name": random.choice(names)}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}

