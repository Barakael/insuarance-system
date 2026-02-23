from database.session import SessionLocal
from models.user import User

class UserService:
    def __init__(self):
        self.db = None

    def authenticate_user(self, username, password):
        # Initialize the session
        self.db = SessionLocal()
        try:
            # Look for the user
            user = self.db.query(User).filter(
                User.username == username, 
                User.password == password
            ).first()
            return user
        except Exception as e:
            print(f"Database error: {e}")
            return None
        # Note: We don't close here because the GUI wants to call close_session later

    def close_session(self):
        # This is the method the GUI was looking for
        if self.db:
            self.db.close()
            print("Database session closed.")

    def create_user(self, username, password, role):
        db = SessionLocal()
        try:
            new_user = User(username=username, password=password, role=role)
            db.add(new_user)
            db.commit()
            print(f"User {username} added to database.")
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            db.rollback()
            return False
        finally:
            db.close()