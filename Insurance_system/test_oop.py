from models.claim_status import ClaimStatus
from models.accident_claim import AccidentClaim
from models.theft_claim import TheftClaim
from models.general_claim_processor import GeneralClaimProcessor
from models.home_policy import HomePolicy
from models.life_policy import LifePolicy
from models.car_policy import CarPolicy
from models.health_policy import HealthPolicy

# Test polymorphism in claims
print("=== Testing Claim Polymorphism ===")
accident_claim = AccidentClaim("A001", "2026-02-23", 50000, "Car accident", "major")
theft_claim = TheftClaim("T001", "2026-02-23", 30000, "Stolen items", ["laptop", "phone", "wallet"])

claims = [accident_claim, theft_claim]
for claim in claims:
    print(f"{type(claim).__name__} Compensation: {claim.calculate_compensation()}")

# Test claim processing stages
print("\n=== Testing Claim Processing Stages ===")
processor = GeneralClaimProcessor("P001", "John Processor")
processor.submit_claim(accident_claim)
print(f"After submit: {accident_claim.view_claim_details()}")

processor.review_claim(accident_claim)
print(f"After review: {accident_claim.view_claim_details()}")

processor.approve_claim(accident_claim)
print(f"After approve: {accident_claim.view_claim_details()}")

# Test policy polymorphism
print("\n=== Testing Policy Polymorphism ===")
policies = [
    LifePolicy("L001", "2026-01-01", "2036-01-01", 35, 1000000, "Jane Doe"),
    CarPolicy("C001", "2026-01-01", "2027-01-01", "ABC123", 500000, "sedan"),
    HealthPolicy("H001", "2026-01-01", "2027-01-01", "comprehensive", "Global Network", 200000),
    HomePolicy("HM001", "2026-01-01", "2027-01-01", 300000, "house", "urban area")
]

for policy in policies:
    print(f"{type(policy).__name__} Premium: {policy.calculate_premium()}")

print("\nSystem started successfully! OOP principles demonstrated.")