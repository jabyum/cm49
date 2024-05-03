from fastapi import Request, Body, UploadFile, APIRouter
from database.postservice import *
from urllib import request

posts_router = APIRouter(prefix="/posts",
                         tags=["Управление постами"])
# добавить пост
@posts_router.post("/api/add_post")
async def add_post(user_id: int, main_text: str, hashtag: str = None):
    new_post = public_post_db(user_id=user_id, main_text=main_text,
                              hashtag=hashtag)
    if new_post:
        return {"status": 1, "message": "Пост успешно создан"}
    return {"status": 0, "message": "Не удалось создать пост"}
# получить все или определенный пост
@posts_router.get("/api/posts")
async def get_all_or_exact_post(post_id=0):
    post = get_all_or_exact_post_db(post_id)
    if post:
        return {"status": 1, "message": post}
    return {"status": 0, "message": "Пост не найден"}
# изменить пост
@posts_router.put("/api/posts")
async def change_user_post(post_id: int, text: str):
    if post_id and text:
        change_post_text(post_id=post_id, new_text=text)
        return {"status": 1, "message": "Пост успешно изменен"}
    return {"status": 0, "message": "Ошибка"}
@posts_router.delete("/api/posts")
async def delete_user_post(user_id: int):
    try:
        delete_post_db(user_id)
        return {"status": 1, "message": "Пост успешно удален"}
    except:
        return {"status": 0, "message": "Не удалось удалить пост"}
