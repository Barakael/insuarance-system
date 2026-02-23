from database.session import SessionLocal
from models.user import User

class UserService:
    def __init__(self):
        self.__session = SessionLocal()

    def create_user(self, username, password, role):
        new_user = User(
            username=username,
            password=password,
            role=role
        )
        self.__session.add(new_user)
        self.__session.commit()
        print("User created successfully!")

    def authenticate_user(self, username, password):
        user = self.__session.query(User).filter_by(
            username=username,
            password=password
        ).first()
        if user:
            return user
        else:
            return None

    def close_session(self):
        self.__session.close()