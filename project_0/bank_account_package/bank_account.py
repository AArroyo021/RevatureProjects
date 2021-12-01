"""
Set a random number of # digits as account ID (no 2 ID's can be the same)

BankAccount should have customer balance,
    Should have the ability to withdraw, deposit

"""
class BankAccount:
    def __init__(self, balance: float, bank_account_num: int):
        self.balance = balance
        self.bank_account_num = bank_account_num

    def __str__(self):
        return "Balance: {}, Bank Account Number: {}".format(self.balance, self.bank_account_num)

    def make_bank_account_dictionary(self):
        return {
            "balance": self.balance,
            "bankAccount": self.bank_account_num
        }
