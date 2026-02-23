from database.base import Base
from database.session import engine

# Import models so they register with Base
from models.user import User

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")