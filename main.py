from fastapi import FastAPI
from database import Base, engine
from api.photo_api.photo import photo_router
# подключение к проекту базы данных и создание всех таблиц
Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url="/")
app.include_router(photo_router)




