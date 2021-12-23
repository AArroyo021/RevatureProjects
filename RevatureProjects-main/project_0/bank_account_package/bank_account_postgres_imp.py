from project_0.bank_account_package.bank_account import BankAccount
from project_0.bank_account_package.bank_account_imp import BankAccountImp
from three_tiered_webapp_example.util.database_connection import connection


class BankAccountPostgresImp(BankAccountImp):

    def create_bank_account(self, bank_account: BankAccount):
        sql = "insert into bank_account values(%s, default, %s) returning bank_account_num"
        cursor = connection.cursor()
        cursor.execute(sql, (bank_account.balance, bank_account.customer_id))
        connection.commit()
        bank_account_id = cursor.fetchone()[0]
        bank_account.bank_account_num = bank_account_id
        return bank_account

    def get_bank_account_info(self, bank_account_num: int):
        sql = "select * from bank_account where bank_account_num = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [bank_account_num])
        bank_account_record = cursor.fetchone()
        bank_account = BankAccount(*bank_account_record)
        return bank_account

    def update_bank_account_info(self, bank_account: BankAccount):
        sql = "update bank_account set balance = %s where bank_account_num = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (bank_account.balance, bank_account.bank_account_num))
        connection.commit()
        return bank_account

    def delete_bank_account_info(self, bank_account_num: int):
        sql = "delete from bank_account where bank_account_num = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [bank_account_num])
        connection.commit()
        return True

    def transfer_funds_between_accounts(self, transfer_amount, transfer_account, receive_account):
        sql = "update bank_account set balance = balance - %s where bank_account_num = %s"
        sql_2 = "update bank_account set balance = balance + %s where bank_account_num = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (transfer_amount, transfer_account))
        cursor.execute(sql_2, (transfer_amount, receive_account))
        connection.commit()
        return receive_account

    def account_withdrawal(self, withdraw_amount, bank_account_num: int):
        sql = "update bank_account set balance = balance - %s where bank_account_num = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (withdraw_amount, bank_account_num))
        connection.commit()
        return bank_account_num

    def account_deposit(self, deposit_amount, bank_account_num: int):
        sql = "update bank_account set balance = balance + %s where bank_account_num = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (deposit_amount, bank_account_num))
        connection.commit()
        return bank_account_num

    def get_all_accounts_from_customer(self, customer_id):
        sql = "select * from bank_account where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        bank_account_record = cursor.fetchall()
        bank_account_list = []
        for bank_account in bank_account_record:
            bank_account_list.append(BankAccount(*bank_account))
        return bank_account_list

    def get_all_bank_accounts(self):
        sql = "select * from bank_account"
        cursor = connection.cursor()
        cursor.execute(sql)
        bank_account_record = cursor.fetchall()
        bank_account_list = []
        for bank_account in bank_account_record:
            bank_account_list.append(BankAccount(*bank_account))
        return bank_account_list