from fastapi import FastAPI
from enum import Enum
from typing import Union
from day2 import Student

class RuchikasFavFood (str,Enum):
    Biryani = "Biryani"
    Chinese = "Chinese"
    Homefood = "HomeFood"



app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/food/{fav_food}")
async def get_food(fav_food:RuchikasFavFood):
    if fav_food is  RuchikasFavFood.Biryani:
        return {"fav_food":fav_food, "Message":"It is a good day"}

    if fav_food.value == "Chinese":
        return {"fav_food":fav_food, "Message":"It is an avg day"}

    return {"fav_food":fav_food, "Message":"It is bad day"}


@app.get("/users/me")
async def admin():
    return {"message":"THIS IS THE OWNER"}


@app.get("/users/{user_id}")
async def get_user(user_id:int):
    return {"user_id": user_id}

@app.post("/")
async def post():
    return {"message":"hello from post route"}

@app.put("/")
async def put():
    return {"message":"hello from put route"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
ruchika_list = [{"shampoo":"loreal"},{"conditioner":"loreal"},{"hairwas":"mamaearth"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return ruchika_list[skip : skip + limit]

@app.get("/items/{item_id}")
async def get_item(item_id:str, q:Union[str,None]= None, short:bool = False):
   item = {"item_id":item_id}
   if q:
      item.update({"q":q})
   if short:
        item.update({"short":"true"})
   if not short:
        item.update({"short":"false"})
   return item

@app.get("/list/{list_id}")
async def list_items(list_id:str, query_param:str, needy:str, q:Union[str,None]= None ):
    list= {"list_id":list_id,"query_param":query_param,"needy":needy}
    if q:
        list.update({"q":q})
    return list

@app.post("/student")
async def student_list(student:Student):
    student_dict = student.dict()
    if student.rollnumber:
        cdnumber = student.rollnumber + student.regnumber
        student_dict.update({"cdnumber":cdnumber})
        return student_dict
