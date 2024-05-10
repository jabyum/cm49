from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# создаем ссылку для подключения/создания базы данных
SQLALCHEMY_DATABASE_URL = "sqlite:///data.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost/social_media49"
                                        #login   пароль  хост    название бд
# создаем движок для работы базы данных
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# создаем переменную для подключений(сессий)
SessionLocal = sessionmaker(bind=engine)
# создаем шаблон для базы данных
Base = declarative_base()
# создаем функцию, которая будет предоставлять сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
