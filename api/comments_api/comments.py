from fastapi import Request, APIRouter
from database.postservice import *
comment_router = APIRouter(prefix="/comment", tags=["Управление комментариями"])
