from .claim_processor import ClaimProcessor
from .claim_status import ClaimStatus

class GeneralClaimProcessor(ClaimProcessor):
    def submit_claim(self, claim):
        claim.update_claim_status(ClaimStatus.SUBMITTED)

    def review_claim(self, claim):
        claim.update_claim_status(ClaimStatus.UNDER_REVIEW)

    def approve_claim(self, claim):
        claim.update_claim_status(ClaimStatus.APPROVED)

    def reject_claim(self, claim):
        claim.update_claim_status(ClaimStatus.REJECTED)