from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from database.session import Base
from datetime import datetime

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(Integer, ForeignKey("policies.id"))
    amount = Column(Float)
    description = Column(String)
    status = Column(String, default="Submitted") # Submitted, Under Review, Approved, Paid
    date_filed = Column(DateTime, default=datetime.utcnow)