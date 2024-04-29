from database import get_db
from database.models import UserPost, Comment, Hashtag, PostPhoto
from datetime import datetime

# Получение всех или одного конкретного поста
def get_all_or_exact_post_db(post_id):
    pass

# редактирование поста
def change_post_text_db(post_id, new_text):
    pass
# удаление поста
def delete_post_db(post_id):
    pass
# публикация поста
def public_post_db(user_id, main_text, hashtag=None):
    pass
# добавление комментария
def public_comment_db(user_id, post_id, text):
    pass
# получение комментариев
def get_exact_post_comment_db(post_id):
    pass
# измение текста комментария
def change_comment_text_db(comment_id, new_text):
    pass
# удаление комментария
def delete_exact_comment_db(comment_id):
    pass
# создание хэштэга
def add_hashtag(name):
    db = next(get_db())
    new_hashtag = Hashtag(hashtag_name=name, reg_date=datetime.now())
    db.add(new_hashtag)
    db.commit()
    return True
# получение определенного хэштега
def get_exact_hashtag_db(hashtag_name):
    db = next(get_db())
    exact_hashtag = db.query(UserPost).filter_by(hashtag=hashtag_name).all()
    return exact_hashtag
# получение рекомендаций по хэштегам
def get_some_hashtag_db(size, hashtag_name):
    db = next(get_db())
    posts = db.query(UserPost).filter_by(hashtag=hashtag_name).all()
    return posts[:size]




