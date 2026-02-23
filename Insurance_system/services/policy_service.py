from database.session import SessionLocal
from models.user import User

class UserService:
    def authenticate_user(self, username, password):
        # We open a new database session
        db = SessionLocal()
        try:
            # Look for the user in the database
            user = db.query(User).filter(
                User.username == username, 
                User.password == password
            ).first()
            return user
        except Exception as e:
            print(f"Database error during login: {e}")
            return None
        finally:
            db.close()