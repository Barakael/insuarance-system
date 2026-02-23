from database.session import engine, Base
from models.user import User
from database.session import SessionLocal

print("Attempting to create tables...")
Base.metadata.create_all(bind=engine)
print("Tables created.")

db = SessionLocal()
admin = db.query(User).filter(User.username == "admin").first()
if not admin:
    new_admin = User(username="admin", password="admin123", role="admin")
    db.add(new_admin)
    db.commit()
    print("Admin user 'admin' with password 'admin123' created!")
else:
    print("Admin user already exists.")
db.close()
