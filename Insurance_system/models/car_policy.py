from models.policy import Policy

class CarPolicy(Policy):

    def __init__(self, policy_id, start_date, end_date,
                 vehicle_number, vehicle_value, vehicle_type):

        super().__init__(policy_id, "Car", start_date, end_date)

        self.__vehicle_number = vehicle_number
        self.__vehicle_value = vehicle_value
        self.__vehicle_type = vehicle_type

    def calculate_premium(self):
        base_rate = 0.03

        if self.__vehicle_type.lower() == "luxury":
            base_rate = 0.06

        premium = self.__vehicle_value * base_rate
        return premium

    def update_vehicle_details(self, vehicle_number, vehicle_value):
        self.__vehicle_number = vehicle_number
        self.__vehicle_value = vehicle_value