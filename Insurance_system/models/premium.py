class Premium:

    def __init__(self, premium_id, payment_date, amount_paid):
        self.__premium_id = premium_id
        self.__payment_date = payment_date
        self.__amount_paid = amount_paid
        self.__payment_status = "Pending"

    def record_payment(self):
        self.__payment_status = "Paid"

    def check_payment_status(self):
        return self.__payment_status

    def generate_receipt(self):
        return f"Receipt: ID {self.__premium_id}, Amount {self.__amount_paid}, Date {self.__payment_date}"
