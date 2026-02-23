from .policy import Policy

class HomePolicy(Policy):
    def __init__(self, policy_id, start_date, end_date, property_value, property_type, location):
        super().__init__(policy_id, "home", start_date, end_date)
        self.__property_value = property_value
        self.__property_type = property_type
        self.__location = location

    def calculate_premium(self):
        base_premium = self.__property_value * 0.005  # 0.5% of property value
        if self.__property_type == "apartment":
            base_premium *= 0.9
        elif self.__property_type == "house":
            base_premium *= 1.1
        # Location risk factor
        if "urban" in self.__location.lower():
            base_premium *= 1.2
        return base_premium