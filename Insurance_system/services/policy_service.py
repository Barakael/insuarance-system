from database.session import SessionLocal
from models.policy import Policy, AutoPolicy, LifePolicy

class PolicyService:
    def get_all_policies(self):
        db = SessionLocal()
        try:
            # We query the base Policy class to get all types
            return db.query(Policy).all()
        finally:
            db.close()

    def create_policy(self, holder, p_type, premium):
        db = SessionLocal()
        try:
            # Polymorphism in action: 
            # We choose the class based on the input type
            if p_type == "Auto":
                new_p = AutoPolicy(holder=holder, type=p_type, premium=float(premium))
            elif p_type == "Life":
                new_p = LifePolicy(holder=holder, type=p_type, premium=float(premium))
            else:
                # Default back to a class that isn't abstract if needed
                # or just use AutoPolicy as a fallback
                new_p = AutoPolicy(holder=holder, type=p_type, premium=float(premium))

            db.add(new_p)
            db.commit()
            return True
        except Exception as e:
            print(f"Error saving: {e}")
            db.rollback()
            return False
        finally:
            db.close()