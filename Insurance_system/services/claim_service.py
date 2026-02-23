from database.session import SessionLocal
from models.claim import Claim # Ensure this model exists
from datetime import datetime

class ClaimService:
    def get_all_claims(self):
        db = SessionLocal()
        try:
            return db.query(Claim).all()
        finally:
            db.close()

    def create_claim(self, policy_id, amount, description):
        db = SessionLocal()
        try:
            new_claim = Claim(
                policy_id=policy_id,
                amount=float(amount),
                description=description,
                status="Submitted",
                date_filed=datetime.now()
            )
            db.add(new_claim)
            db.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            db.rollback()
            return False
        finally:
            db.close()

    def update_status(self, claim_id, new_status):
        db = SessionLocal()
        try:
            claim = db.query(Claim).filter(Claim.id == claim_id).first()
            if claim:
                claim.status = new_status
                db.commit()
                return True
            return False
        finally:
            db.close()

    def delete_claim(self, claim_id):
        db = SessionLocal()
        try:
            claim = db.query(Claim).filter(Claim.id == claim_id).first()
            if claim:
                db.delete(claim)
                db.commit()
                return True
            return False
        finally:
            db.close()