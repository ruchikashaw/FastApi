# 28th feb 2023
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"HelloWorld"}

# @app.get("/items/{item_id}")
# async def items(item_id:int):
#     return {"item_id":item_id}

@app.get("/ruchikaloves/loves")
async def loves(loves:str):
    return{"loves":loves}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None





@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result