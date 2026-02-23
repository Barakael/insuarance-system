from database.session import SessionLocal
from models.policy import Policy
from models.claim import Claim
from sqlalchemy import func

class DashboardService:
    def get_stats(self):
        db = SessionLocal()
        try:
            # Count total policies
            total_policies = db.query(Policy).count()
            
            # Count total claims
            total_claims = db.query(Claim).count()
            
            # Calculate total revenue (Sum of all premiums)
            total_revenue = db.query(func.sum(Policy.premium)).scalar() or 0.0
            
            # Calculate total payouts (Sum of approved/paid claims)
            total_payouts = db.query(func.sum(Claim.amount)).filter(
                Claim.status.in_(["Approved", "Paid"])
            ).scalar() or 0.0

            return {
                "policies": total_policies,
                "claims": total_claims,
                "revenue": f"${total_revenue:,.2f}",
                "payouts": f"${total_payouts:,.2f}"
            }
        finally:
            db.close()