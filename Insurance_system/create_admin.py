from database.session import SessionLocal
from models.user import User

session = SessionLocal()

admin = User(
    username="admin",
    password="admin123",
    role="admin"
)

session.add(admin)
session.commit()

print("Admin created successfully!")