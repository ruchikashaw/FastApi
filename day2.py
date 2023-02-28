from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


class Student (BaseModel):
    name: str
    rollnumber: int
    regnumber: int
    branch: str
    bloodgroup: Union[str, None] = None

