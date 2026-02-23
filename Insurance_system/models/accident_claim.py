from .claim import Claim

class AccidentClaim(Claim):
    def __init__(self, claim_id, claim_date, claim_amount, description, vehicle_damage):
        super().__init__(claim_id, claim_date, claim_amount, description)
        self.__vehicle_damage = vehicle_damage

    def calculate_compensation(self):
        # Example: compensation based on damage severity
        if self.__vehicle_damage == "minor":
            return self._Claim__claim_amount * 0.5
        elif self.__vehicle_damage == "major":
            return self._Claim__claim_amount * 0.8
        else:
            return self._Claim__claim_amount