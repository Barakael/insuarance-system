from database import engine, Base, SessionLocal
from models.user import User

def initialize():
    # 1. Create the tables
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)

    # 2. Create the admin user
    db = SessionLocal()
    
    # Check if admin already exists
    admin_exists = db.query(User).filter(User.username == "admin").first()
    
    if not admin_exists:
        print("Creating admin user...")
        new_user = User(
            username="admin",
            password="admin123",
            role="admin"
        )
        db.add(new_user)
        db.commit()
        print("Done! You can now log in with admin/admin123")
    else:
        print("Admin already exists.")
    
    db.close()

if __name__ == "__main__":
    initialize()
    