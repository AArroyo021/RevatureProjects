from project_0.bank_account_package.bank_account import BankAccount
from project_0.bank_account_package.bank_account_abstract import BankAccountAbs


class BankAccountImp(BankAccountAbs):
    bank_account_ex = BankAccount(1234.56, 0)
    bank_account_list = [bank_account_ex]
    account_num_for_now = 0

    def create_bank_account(self, bank_account: BankAccount):
        bank_account.bank_account_num = BankAccountImp.account_num_for_now
        BankAccountImp.account_num_for_now += 1
        BankAccountImp.bank_account_list.append(bank_account)
        return bank_account

    def get_bank_account_info(self, bank_account_num: int):
        for bank_account in BankAccountImp.bank_account_list:
            if bank_account.bank_account_num == bank_account_num:
                return bank_account

    def update_bank_account_info(self, bank_account: BankAccount):
        for bank_account_in_list in BankAccountImp.bank_account_list:
            if bank_account_in_list.bank_account_num == bank_account.bank_account_num:
                index = BankAccountImp.bank_account_list.index(bank_account_in_list)
                BankAccountImp.bank_account_list[index] = bank_account
                return bank_account

    def delete_bank_account_info(self, bank_account_num: int):
       for bank_account_in_list in BankAccountImp.bank_account_list:
           if bank_account_in_list.bank_account_num == bank_account_num:
               index = BankAccountImp.bank_account_list.index(bank_account_in_list)
               del BankAccountImp.bank_account_list[index]
               return bool
