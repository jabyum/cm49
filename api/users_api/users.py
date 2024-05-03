from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import List, Dict
from database.userservice import *
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def mail_checker(email):
    if re.fullmatch(regex, email):
        return True
    return False
class User(BaseModel):
    name: str
    email: str
    phone_number: str
    password: str
    user_city: str | None = None
    birthday: str | None = None

users_router = APIRouter(tags=["Управление юзерами"], prefix="/users")

@users_router.post("/api/registration")
async def register_user(user_model: User):
    user_data = dict(user_model)
    mail_validation = mail_checker(user_model.email)
    if mail_validation:
        try:
            reg_user = register_user_db(**user_data)
            return {"status": 1, "message": reg_user}
        except Exception as e:
            return {"status": 0 , "message": e}

    return {"status": 0, "message": "Invalid email or phone"}







