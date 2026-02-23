from models.policy import Policy

class LifePolicy(Policy):

    def __init__(self, policy_id, start_date, end_date, insured_age, coverage_amount, beneficiary_name):
        super().__init__(policy_id, "Life", start_date, end_date)

        self.__insured_age = insured_age
        self.__coverage_amount = coverage_amount
        self.__beneficiary_name = beneficiary_name

    # Implement abstract method
    def calculate_premium(self):
        base_rate = 0.05

        if self.__insured_age > 50:
            base_rate = 0.08

        premium = self.__coverage_amount * base_rate
        return premium

    def get_beneficiary(self):
        return self.__beneficiary_name