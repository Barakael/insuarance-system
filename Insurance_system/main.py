#from models.policy import Policy
#
#from models.life_policy import LifePolicy

# Create life policy object

#life_policy = LifePolicy(
   # policy_id=101,
   # start_date="2026-01-01",
   # end_date="2036-01-01",
   # insured_age=30,
   # coverage_amount=1000000,
   # beneficiary_name="John Doe"
#)

#premium = life_policy.calculate_premium()

#print("Calculated Premium:", premium)#
#from models.car_policy import CarPolicy

'''car_policy = CarPolicy(
    policy_id=202,
    start_date="2026-01-01",
    end_date="2027-01-01",
    vehicle_number="T123ABC",
    vehicle_value=50000000,
    vehicle_type="Luxury"
)

premium = car_policy.calculate_premium()

print("Car Policy Premium:", premium)'''
#from models.health_policy import HealthPolicy

'''health_policy = HealthPolicy(
    policy_id=303,
    start_date="2026-01-01",
    end_date="2027-01-01",
    coverage_type="International",
    hospital_network="Global Hospitals",
    medical_limit=20000000
)

premium = health_policy.calculate_premium()

print("Health Policy Premium:", premium)'''

'''from models.customer import Customer
from models.life_policy import LifePolicy
from models.car_policy import CarPolicy

# Create customer
customer = Customer(
    customer_id=1,
    name="Kelvin",
    phone_number="0712345678",
    email="kelvin@email.com",
    address="Dar es Salaam"
)

# Create policies
life_policy = LifePolicy(
    policy_id=101,
    start_date="2026-01-01",
    end_date="2036-01-01",
    insured_age=30,
    coverage_amount=1000000,
    beneficiary_name="John Doe"
)

car_policy = CarPolicy(
    policy_id=202,
    start_date="2026-01-01",
    end_date="2027-01-01",
    vehicle_number="T123ABC",
    vehicle_value=50000000,
    vehicle_type="Luxury"
)

# Associate policies with customer
customer.add_policy(life_policy)
customer.add_policy(car_policy)

# Show policies
policies = customer.view_policies()

print("Customer:", customer.get_name())
print("Number of policies:", len(policies))

for policy in policies:
    print("Premium:", policy.calculate_premium())'''

'''from models.life_policy import LifePolicy
from models.premium import Premium

life_policy = LifePolicy(
    policy_id=101,
    start_date="2026-01-01",
    end_date="2036-01-01",
    insured_age=30,
    coverage_amount=1000000,
    beneficiary_name="John Doe"
)

# Create premium payment
premium1 = Premium(
    premium_id=1,
    payment_date="2026-02-01",
    amount_paid=50000
)

# Record payment
premium1.record_payment()

# Attach to policy
life_policy.add_premium(premium1)

# Check
for p in life_policy.get_premiums():
    print(p.generate_receipt())
    print("Status:", p.check_payment_status())
'''
'''from models.life_policy import LifePolicy
from models.claim import Claim
from models.claim_processor import ClaimProcessor

# Create policy
life_policy = LifePolicy(
    policy_id=101,
    start_date="2026-01-01",
    end_date="2036-01-01",
    insured_age=30,
    coverage_amount=1000000,
    beneficiary_name="John Doe"
)

# Create claim
claim1 = Claim(
    claim_id=1,
    claim_date="2026-03-01",
    claim_amount=200000,
    description="Hospital expenses"
)

# Attach claim to policy
life_policy.add_claim(claim1)

# Process claim
processor = ClaimProcessor(1, "Mr. Manager")

if processor.verify_claim(claim1):
    processor.approve_claim(claim1)

# Show result
for c in life_policy.get_claims():
    print(c.view_claim_details())'''

'''from gui.main_window import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.run()'''

'''import tkinter as tk
from gui.login_window import LoginWindow

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()'''

'''from services.user_service import create_user

create_user("admin", "1234", "admin")'''

'''from services.user_service import authenticate_user

user = authenticate_user("admin", "1234")

if user:
    print("Login successful!")
else:
    print("Invalid credentials!")'''

'''from gui.login_window import LoginWindow

LoginWindow()'''

import tkinter as tk
from gui.login_window import LoginWindow


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()