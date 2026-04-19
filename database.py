from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Создаем файл базы данных blog.db
engine = create_engine("sqlite:///blog.db")
SessionLocal = sessionmaker(bind=engine)