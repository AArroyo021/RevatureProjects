"""
Class to save customers personal information:
    Name
        First
        Last
    Account Num
"""

class Customer:
    def __init__(self, first_name: str, last_name: str, bank_account: [int], customer_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.bank_account = bank_account
        self.customer_id = customer_id

    def make_person_dictionary(self):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "bankAccount": self.bank_account,
            "customerId": self.customer_id
        }

    def __str__(self):
        return "First Name: {}, Last Name: {}, Bank Account Number: {}, Customer ID: {}".format(self.first_name, self.last_name, self.bank_account, self.customer_id)
