from abc import ABC, abstractmethod

class Policy(ABC):
    
    def __init__(self, policy_id, policy_type, start_date, end_date):
        # Encapsulation (private attributes)
        self.__policy_id = policy_id
        self.__policy_type = policy_type
        self.__start_date = start_date
        self.__end_date = end_date
        self.__active = False
        self.__premiums = []
        self.__claims = []



    # Getter methods
    def get_policy_id(self):
        return self.__policy_id

    def get_policy_type(self):
        return self.__policy_type

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def is_active(self):
        return self.__active

    # Business methods
    def activate_policy(self):
        self.__active = True
        print("Policy activated successfully.")

    def cancel_policy(self):
        self.__active = False
        print("Policy cancelled successfully.")
        
    def add_premium(self, premium):
        self.__premiums.append(premium)

    def get_premiums(self):
        return self.__premiums
    def add_claim(self, claim):
        self.__claims.append(claim)

    def get_claims(self):
        return self.__claims



    # Abstract method (Polymorphism will happen here)
    @abstractmethod
    def calculate_premium(self):
        pass