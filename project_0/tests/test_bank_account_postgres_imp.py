from project_0.bank_account_package.bank_account import BankAccount
from project_0.bank_account_package.bank_account_logic import BankAccountLogic
from project_0.bank_account_package.bank_account_postgres_imp import BankAccountPostgresImp

bank_account_postgres_imp = BankAccountPostgresImp()
bank_account = BankAccount(1000.32, 0, 1)
bank_account_postgres_logic = BankAccountLogic(bank_account_postgres_imp)
logic_account = BankAccount(5000.66, 0, 1)
logic_account_update = BankAccount(6000, 10, 1)

def test_create_bank_account():
    new_bank_account: BankAccount = bank_account_postgres_imp.create_bank_account(bank_account)
    assert new_bank_account.bank_account_num != 1

def test_get_bank_account_info():
    return_bank_account: BankAccount = bank_account_postgres_imp.get_bank_account_info(2)
    assert return_bank_account.bank_account_num == 2

def test_update_bank_account_info():
    update_examp = BankAccount(9875.45, 5, 1)
    updated_bank_account: BankAccount = bank_account_postgres_imp.update_bank_account_info(update_examp)
    assert updated_bank_account.bank_account_num == updated_bank_account.bank_account_num

def test_delete_bank_account_info():
    remove_bank_account = bank_account_postgres_imp.delete_bank_account_info(6)
    assert remove_bank_account

def test_transfer_funds_between_accounts():
    transfer_bank_account_funds = bank_account_postgres_imp.transfer_funds_between_accounts(100, 4, 7)
    assert transfer_bank_account_funds

def test_get_all_accounts_from_customer():
    return_bank_accounts = bank_account_postgres_imp.get_all_accounts_from_customer(1)
    assert return_bank_accounts

def test_get_all_bank_accounts():
    return_all_bank_accounts = bank_account_postgres_imp.get_all_bank_accounts()
    assert return_all_bank_accounts

"""********************************** Logic Tests ***********************************"""

def test_service_create_bank_account():
    try:
        bank_account_postgres_logic.service_create_bank_account(logic_account)
        assert False
    except Exception as e:
        assert str(e) == "This account number already exists"

def test_service_update_bank_account_info():
    try:
        bank_account_postgres_logic.service_update_bank_account_info(logic_account_update)
        assert False
    except Exception as e:
        assert str(e) == "This account is not part of this customer"

def test_service_transfer_funds_between_accounts():
    transfer_amount = 100
    transfer_account = 13
    receive_account = 10

    try:
        bank_account_postgres_logic.service_transfer_funds_between_accounts(transfer_amount, transfer_account, receive_account)
        assert False
    except Exception as e:
        assert str(e) == "The accounts aren't part of the same customer or there aren't enough funds in the account"

def test_service_account_withdrawal():
    try:
        bank_account_postgres_logic.service_account_withdrawal(100, 12)
        assert False
    except Exception as e:
        assert str(e) == "Trying to withdraw negative amounts" or "Not enough funds to withdraw"

def test_service_account_deposit():
    try:
        bank_account_postgres_logic.service_account_deposit(100, 2)
        assert False
    except Exception as e:
        assert str(e) == "Trying to deposit negative amounts"