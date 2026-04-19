About this project:
This is a simple backend for a blog. It helps manage users, their personal profiles, blog posts, and tags.

Database Models and Relationships:
1. User and Profile: One to One (1:1). Each user has only one personal bio.
2. User and Post: One to Many (1:N). One author can write many different posts.
3. Post and Tag: Many to Many (N:N). Posts can have multiple tags, and tags can belong to many posts.

How to start:
1. Install SQLAlchemy using the command: "pip install sqlalchemy"
2. Run the main script using the command: "python main.py"
3. The database file blog.db will be created automatically in your folder.

Project Structure:
models.py: Contains database tables and relationships.
database.py: Contains connection settings for SQLite.
main.py: Script to create data and run search queries.
