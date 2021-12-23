from project_0.bank_account_package.bank_account import BankAccount
from project_0.bank_account_package.bank_account_imp import BankAccountImp

bank_account_imp = BankAccountImp()
bank_account = BankAccount(1000.32, 0)

def test_create_bank_account():
    new_bank_account: BankAccount = bank_account_imp.create_bank_account(bank_account)
    assert new_bank_account.bank_account_num != 1

def test_get_bank_account_info():
    return_bank_account: BankAccount = bank_account_imp.get_bank_account_info(0)
    assert return_bank_account.bank_account_num == 0

def test_update_bank_account_info():
    update_examp = BankAccount(9875.45, 0)
    updated_bank_account: BankAccount = bank_account_imp.update_bank_account_info(update_examp)
    assert updated_bank_account.bank_account_num == updated_bank_account.bank_account_num

def test_delete_bank_account_info():
    remove_bank_account = bank_account_imp.delete_bank_account_info(0)
    assert remove_bank_account