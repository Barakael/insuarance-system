import tkinter as tk
from gui.login_window import LoginWindow
from database.session import engine, Base, SessionLocal
from models.user import User # This import MUST be here for SQLAlchemy to see the table

def init_db():
    print("Initializing database...")
    # This line physically creates the 'users' table in your .db file
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        # Create a default admin if one doesn't exist
        admin = db.query(User).filter(User.username == "admin").first()
        if not admin:
            new_admin = User(username="admin", password="admin123", role="admin")
            db.add(new_admin)
            db.commit()
            print("Default admin created successfully.")
        else:
            print("Admin user already exists.")
    except Exception as e:
        print(f"Error during DB init: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    # 1. Setup the Database first
    init_db()
    
    # 2. Launch the UI
    root = tk.Tk()
    root.title("Insurance Management System")
    app = LoginWindow(root)
    root.mainloop()