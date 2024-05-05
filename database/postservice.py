from database import get_db
from database.models import UserPost, Comment, Hashtag, PostPhoto
from datetime import datetime

# Getting data about a post
def get_all_or_exact_post_db(post_id: int):
    db = next(get_db())
    if post_id != 0:
        exact_post = db.query(UserPost).filter_by(id=post_id).first()
        return exact_post
    elif post_id == 0:
        all_posts = db.query(UserPost).all()
        return [i for i in all_posts]

# Redacting a post
def change_post_text(post_id, new_text):
    db = next(get_db())
    post_to_edit = db.query(UserPost).filter_by(id=post_id).first()
    if post_to_edit:
        post_to_edit.main_text = new_text
        db.commit()
        return True
    return False

# Deleting a post
def delete_post_db(post_id):
    db = next(get_db())
    post_to_delete = db.query(UserPost).filter_by(id=post_id).first()
    if post_to_delete:
        db.delete(post_to_delete)
        db.commit()
        return True
    return False

# Publishing a post
def public_post_db(user_id, main_text, hashtag=None):
    db = next(get_db())
    new_post = UserPost(user_id=user_id, main_text=main_text, reg_date=datetime.now(), hashtag=hashtag)
    db.add(new_post)
    db.commit()
    return True

# Adding a comment
def public_comment_db(user_id, post_id, text):
    db = next(get_db())
    new_comment = Comment(user_id=user_id, post_id=post_id, text=text, created_at=datetime.now())
    db.add(new_comment)
    db.commit()
    return True

# Getting comments for a specific post
def get_exact_post_comment_db(post_id):
    db = next(get_db())
    exact_comments = db.query(Comment).filter_by(post_id=post_id).all()
    return exact_comments

# Changing text of a comment
def change_comment_text_db(comment_id, new_text):
    db = next(get_db())
    comment_to_edit = db.query(Comment).filter_by(id=comment_id).first()
    if comment_to_edit:
        comment_to_edit.text = new_text
        db.commit()
        return True
    return False

# Deleting a comment
def delete_exact_comment_db(comment_id):
    db = next(get_db())
    comment_to_delete = db.query(Comment).filter_by(id=comment_id).first()
    if comment_to_delete:
        db.delete(comment_to_delete)
        db.commit()
        return True
    return False

# Creating a hashtag
def add_hashtag(name):
    db = next(get_db())
    new_hashtag = Hashtag(hashtag_name=name, reg_date=datetime.now())
    db.add(new_hashtag)
    db.commit()
    return True

# Getting exact hashtag
def get_exact_hashtag_db(hashtag_name):
    db = next(get_db())
    exact_hashtag = db.query(Hashtag).filter_by(hashtag_name=hashtag_name).first()
    return exact_hashtag

# Getting recommendations based on hashtag
def get_some_hashtag_db(size, hashtag_name):
    db = next(get_db())
    posts = db.query(UserPost).filter_by(hashtag=hashtag_name).limit(size).all()
    return posts
