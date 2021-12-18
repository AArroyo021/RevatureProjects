from datetime import date


class Reimbursement:
    def __init__(self, claim_num: int, employee_id: int, claim_amount: float, claim_reason: str, claim_status: bool, manager_validation: bool, manager_reasoning: str, date_sent: date, date_validated: date):
        self.claim_num = claim_num
        self.employee_id = employee_id
        self.claim_amount = claim_amount
        self.claim_reason = claim_reason
        self.claim_status = claim_status
        self.manager_validation = manager_validation
        self.manager_reasoning = manager_reasoning
        self.date_sent = date_sent
        self.date_validated = date_validated


    def make_reimbursement_dict(self):
        return {
            "claimNum": self.claim_num,
            "employeeId": self.employee_id,
            "claimAmount": self.claim_amount,
            "claimReason": self.claim_reason,
            "claimStatus": self.claim_status,
            "managerValidation": self.manager_validation,
            "managerReasoning": self.manager_reasoning,
            "dateSent": self.date_sent,
            "dateValidated": self.date_validated
        }