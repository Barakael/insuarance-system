from .claim import Claim

class TheftClaim(Claim):
    def __init__(self, claim_id, claim_date, claim_amount, description, stolen_items):
        super().__init__(claim_id, claim_date, claim_amount, description)
        self.__stolen_items = stolen_items

    def calculate_compensation(self):
        # Example: compensation based on number of stolen items
        return self._Claim__claim_amount * min(len(self.__stolen_items), 5) / 5