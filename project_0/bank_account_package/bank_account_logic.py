from project_0.bank_account_package.bank_account import BankAccount
from project_0.bank_account_package.bank_account_postgres_imp import BankAccountPostgresImp


class BankAccountLogic():
    def __init__(self, bank_imp):
        self.bank_imp: BankAccountPostgresImp = bank_imp

    def service_create_bank_account(self, bank_account: BankAccount):
        for current_account in self.bank_imp.bank_account_list:
            if current_account.bank_account_num == bank_account.bank_account_num:
                raise Exception("This account number already exists")
        else:
            return self.bank_imp.create_bank_account(bank_account)

    def service_get_bank_account_info(self, bank_account_num: int):
        return self.bank_imp.get_bank_account_info(bank_account_num)

    def service_update_bank_account_info(self, bank_account: BankAccount):
        for current_account in self.bank_imp.bank_account_list:
            if current_account.customer_id != bank_account.customer_id:
                raise Exception("This account is not part of this customer")
        else:
            return self.bank_imp.update_bank_account_info(bank_account)

    def service_delete_bank_account_info(self, bank_account_num: int):
        return self.bank_imp.delete_bank_account_info(bank_account_num)

    def service_transfer_funds_between_accounts(self, transfer_amount, transfer_account, receive_account):
        current_transfer_account = self.service_get_bank_account_info(transfer_account)
        current_receive_account = self.service_get_bank_account_info(receive_account)

        if current_transfer_account.customer_id == current_receive_account.customer_id:
            if transfer_amount <= current_transfer_account.balance:
                if transfer_amount >= 0:
                    return self.bank_imp.transfer_funds_between_accounts(transfer_amount, transfer_account, receive_account)
        else:
            raise Exception("The accounts aren't part of the same customer or there aren't enough funds in the account")

    def service_account_withdrawal(self, withdraw_amount, bank_account_num: int):
        current_bank_account = self.service_get_bank_account_info(bank_account_num)
        if withdraw_amount < 0:
            raise Exception("Trying to withdraw negative amounts")
        if withdraw_amount > current_bank_account.balance:
            raise Exception("Not enough funds to withdraw")
        else:
            return self.bank_imp.account_withdrawal(withdraw_amount, bank_account_num)

    def service_account_deposit(self, deposit_amount, bank_account_num: int):
        current_bank_account = self.service_get_bank_account_info(bank_account_num)
        if deposit_amount < 0:
            raise Exception("Trying to deposit negative amounts")
        else:
            return self.bank_imp.account_deposit(deposit_amount, bank_account_num)

    def service_get_all_accounts_from_customer(self, customer_id):
        return self.bank_imp.get_all_accounts_from_customer(customer_id)

    def service_get_all_bank_accounts(self):
        return self.bank_imp.get_all_bank_accounts()