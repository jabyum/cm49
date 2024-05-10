from fastapi import FastAPI, Body

from database import Base, engine
from api.photo_api.photo import photo_router
from api.users_api.users import users_router
from api.posts_api.posts import posts_router
from api.comments_api.comments import comment_router
from api.hashtag_api.hashtag import hashtag_router

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(users_router)
app.include_router(posts_router)
app.include_router(photo_router)
app.include_router(comment_router)
app.include_router(hashtag_router)