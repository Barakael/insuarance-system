from sqlalchemy import Column, Integer, String, Float
from database.session import Base
from abc import ABC, abstractmethod

# 1. The Abstract Base Class (Logic)
class Policy(Base):
    __tablename__ = "policies"
    
    id = Column(Integer, primary_key=True, index=True)
    holder = Column(String)
    type = Column(String) # 'Auto', 'Life', etc.
    premium = Column(Float)
    status = Column(String, default="Active")

    # This makes the class Abstract in OOP
    @abstractmethod
    def calculate_premium(self):
        pass

# 2. The Concrete Classes (Implementation)
# These are what actually get saved to the DB
class AutoPolicy(Policy):
    def calculate_premium(self):
        # Example logic: Auto policies have a base tax
        return self.premium * 1.1

class LifePolicy(Policy):
    def calculate_premium(self):
        # Example logic: Life policies have different risk rates
        return self.premium * 1.2