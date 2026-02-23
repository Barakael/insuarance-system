from models.policy import Policy

class HealthPolicy(Policy):

    def __init__(self, policy_id, start_date, end_date,
                 coverage_type, hospital_network, medical_limit):

        super().__init__(policy_id, "Health", start_date, end_date)

        self.__coverage_type = coverage_type
        self.__hospital_network = hospital_network
        self.__medical_limit = medical_limit

    def calculate_premium(self):
        base_rate = 0.04

        if self.__coverage_type.lower() == "international":
            base_rate = 0.07

        premium = self.__medical_limit * base_rate
        return premium

    def view_coverage_details(self):
        return f"Coverage: {self.__coverage_type}, Network: {self.__hospital_network}"