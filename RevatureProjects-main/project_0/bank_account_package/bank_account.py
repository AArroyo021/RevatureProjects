"""
Set a random number of # digits as account ID (no 2 ID's can be the same)

BankAccount should have customer balance,
    Should have the ability to withdraw, deposit

"""
class BankAccount:
    def __init__(self, balance: float, bank_account_num: int, customer_id: int):
        self.balance = balance
        self.bank_account_num = bank_account_num
        self.customer_id = customer_id

    def make_bank_account_dictionary(self):
        return {
            "balance": self.balance,
            "bankAccountNum": self.bank_account_num,
            "customerId": self.customer_id
        }
    def __str__(self):
        return "Balance: {}, Bank Account Number: {}, Customer Id: {}".format(self.balance, self.bank_account_num, self.customer_id)