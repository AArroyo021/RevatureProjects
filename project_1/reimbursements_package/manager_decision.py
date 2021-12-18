from datetime import date


class ManagerDecision:
    def __init__(self, manager_reasoning: str, date_validated: date):
        self.manager_reasoning = manager_reasoning
        self.date_validated = date_validated