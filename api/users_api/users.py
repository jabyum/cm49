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

@users_router.get("/api/user")
async def get_user(user_id: int):
    exact_user = profile_info_db(user_id)
    if exact_user:
        return {"status": 1, "message": exact_user}
    return {"status": 0, "message": "Пользователь не найден"}

# вход в аккаунт
@users_router.post("/api/login")
async def login_user(login: str, password: str):
    checking = check_user_password_db(login=login, password=password)
    if checking:
        return {"status": 1, "message": checking}
    return {"status": 0, "message": "Ошибка входа"}

# изменение данных
@users_router.put("/api/change_profile")
async def change_user_profile(user_id: int, changeable_info: str, new_data: str):
    data = change_user_data_db(user_id=user_id, changeable_info=changeable_info, new_data=new_data)
    if data:
        return {"status": 1, "message": "Данные успешно изменены"}
    return {"status": 0, "message": "Не удалось изменить информацию"}

@users_router.delete("/api/delete_user")
async def delete_user_post(user_id: int):
    try:
        delete_user_db(user_id)
        return {"status": 1, "message": "Юзер удален"}
    except:
        return {"status": 0, "message": "Не удалось удалить юзера"}


