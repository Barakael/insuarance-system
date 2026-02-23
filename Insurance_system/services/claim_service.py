from database.session import SessionLocal
from models.claim import Claim

class ClaimService:
    def get_claims_by_stage(self, stage):
        db = SessionLocal()
        try:
            if stage == "All":
                return db.query(Claim).all()
            return db.query(Claim).filter(Claim.stage == stage).all()
        finally:
            db.close()