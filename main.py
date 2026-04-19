from database import engine, SessionLocal
from models import Base, User, Profile, Post, Tag

Base.metadata.drop_all(bind=engine) # Стираем старое, если было
Base.metadata.create_all(bind=engine) # Создаем новое

db = SessionLocal()

ivan = User(username="ivan_ivanov", email="ivan@example.com")
ivan_profile = Profile(bio="Люблю программировать на Python", user=ivan)

tag_python = Tag(name="Python")
tag_news = Tag(name="Новости")

post1 = Post(
    title="Мой первый пост", 
    content="SQLAlchemy — это круто!", 
    author=ivan,
    tags=[tag_python, tag_news]
)

db.add_all([ivan, ivan_profile, tag_python, tag_news, post1])
db.commit()

user_to_edit = db.query(User).filter_by(username="ivan_ivanov").first()
user_to_edit.email = "new_ivan@example.com"
db.commit()

print("--- Все посты пользователя ---")
user = db.query(User).get(1)
for p in user.posts:
    print(f"Пост: {p.title}")

print("\n--- Поиск постов с тегом Python ---")
posts_with_tag = db.query(Post).join(Post.tags).filter(Tag.name == "Python").all()
for p in posts_with_tag:
    print(f"Найден пост: {p.title}")

db.close()
