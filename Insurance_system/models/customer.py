class Customer:

    def __init__(self, customer_id, name, phone_number, email, address):
        self.__customer_id = customer_id
        self.__name = name
        self.__phone_number = phone_number
        self.__email = email
        self.__address = address

        # A customer can have multiple policies
        self.__policies = []

    # Add policy to customer
    def add_policy(self, policy):
        self.__policies.append(policy)

    # View all policies
    def view_policies(self):
        return self.__policies

    # Update customer details
    def update_customer_details(self, phone_number, email, address):
        self.__phone_number = phone_number
        self.__email = email
        self.__address = address

    # Getter for name
    def get_name(self):
        return self.__name