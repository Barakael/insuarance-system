from database.session import SessionLocal
from models.policy import Policy

class PolicyService:
    def __init__(self):
        self.__session = SessionLocal()

    def create_policy(self, policy):
        self.__session.add(policy)
        self.__session.commit()
        print("Policy created successfully!")

    def get_policy(self, policy_id):
        return self.__session.query(Policy).filter_by(policy_id=policy_id).first()

    def update_policy(self, policy):
        self.__session.commit()
        print("Policy updated successfully!")

    def close_session(self):
        self.__session.close()