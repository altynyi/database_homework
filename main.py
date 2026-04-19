from database import engine, SessionLocal
from models import Base, User, Profile, Post, Tag

# 1. Создаем таблицы
Base.metadata.drop_all(bind=engine) # Стираем старое, если было
Base.metadata.create_all(bind=engine) # Создаем новое

db = SessionLocal()

# 2. Наполняем данными (Part 4)
# Создаем пользователя с профилем (1:1)
ivan = User(username="ivan_ivanov", email="ivan@example.com")
ivan_profile = Profile(bio="Люблю программировать на Python", user=ivan)

# Создаем теги (N:N)
tag_python = Tag(name="Python")
tag_news = Tag(name="Новости")

# Создаем пост (1:N) и привязываем теги
post1 = Post(
    title="Мой первый пост", 
    content="SQLAlchemy — это круто!", 
    author=ivan,
    tags=[tag_python, tag_news]
)

db.add_all([ivan, ivan_profile, tag_python, tag_news, post1])
db.commit()

# 3. CRUD операции (Part 2)
# Create - уже сделали выше
# Read
user_to_edit = db.query(User).filter_by(username="ivan_ivanov").first()
# Update
user_to_edit.email = "new_ivan@example.com"
db.commit()
# Delete (пример)
# db.delete(user_to_edit)
# db.commit()

# 4. Запросы (Part 3)
print("--- Все посты пользователя ---")
user = db.query(User).get(1)
for p in user.posts:
    print(f"Пост: {p.title}")

print("\n--- Поиск постов с тегом Python ---")
posts_with_tag = db.query(Post).join(Post.tags).filter(Tag.name == "Python").all()
for p in posts_with_tag:
    print(f"Найден пост: {p.title}")

db.close()