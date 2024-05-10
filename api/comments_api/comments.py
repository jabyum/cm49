from fastapi import Request, APIRouter
from database.postservice import *

comment_router = APIRouter(prefix="/comment", tags=["Управление комментариями"])

@comment_router.post('/api/add_comment')
async def add_comment(user_id: int, post_id: int, text: str):
    new_comment = public_comment_db(user_id, post_id, text)
    if new_comment:
        return {'status': 1, 'message': 'Коммент успешно создан'}
    return {'status': 0, 'message': 'Не удалось опубликовать коммент'}


@comment_router.get('/api/get_comment')
async def get_comment(post_id: int):
    comment = get_exact_post_comment_db(post_id)
    if comment:
        return {'status': 1, 'message': comment}
    return {'status': 0, 'message': 'Коммент не найден'}

@comment_router.post('/api/change_comment')
async def change_comment(comment_id: int, new_text: str):
    comment_to_change = change_comment_text_db(comment_id, new_text)
    if comment_to_change:
        return {'status': 1, 'message': 'Коммент успешно изменен'}
    return {'status': 0, 'message': 'Ошибка!'}

@comment_router.delete('/api/delete_comment')
async def del_comment(comment_id: int):
    try:
        delete_exact_comment_db(comment_id)
        return {'status': 1, 'message': 'Коммент успешно удален'}
    except:
        return {'status': 0, 'message': 'Ошибка'}