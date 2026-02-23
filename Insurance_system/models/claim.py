from abc import ABC, abstractmethod
from .claim_status import ClaimStatus

class Claim(ABC):

    def __init__(self, claim_id, claim_date, claim_amount, description):
        self.__claim_id = claim_id
        self.__claim_date = claim_date
        self.__claim_amount = claim_amount
        self.__description = description
        self.__claim_status = ClaimStatus.SUBMITTED

    @abstractmethod
    def calculate_compensation(self):
        pass

    def update_claim_status(self, status):
        self.__claim_status = status

    def view_claim_details(self):
        return f"Claim ID: {self.__claim_id}, Amount: {self.__claim_amount}, Status: {self.__claim_status.value}"
