from database.session import SessionLocal
from models.policy import Policy # Ensure you create this model

class PolicyService:
    def get_all_policies(self):
        db = SessionLocal()
        try:
            return db.query(Policy).all()
        finally:
            db.close()

    def create_policy(self, holder_name, p_type, premium):
        db = SessionLocal()
        try:
            new_policy = Policy(holder=holder_name, type=p_type, premium=premium, status="Active")
            db.add(new_policy)
            db.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            db.close()