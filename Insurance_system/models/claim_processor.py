from abc import ABC, abstractmethod
from .claim_status import ClaimStatus

class ClaimProcessor(ABC):

    def __init__(self, processor_id, processor_name):
        self.__processor_id = processor_id
        self.__processor_name = processor_name

    @abstractmethod
    def submit_claim(self, claim):
        pass

    @abstractmethod
    def review_claim(self, claim):
        pass

    @abstractmethod
    def approve_claim(self, claim):
        pass

    @abstractmethod
    def reject_claim(self, claim):
        pass

    def verify_claim(self, claim):
        # Simple verification logic
        if claim:
            return True
        return False
