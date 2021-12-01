from abc import ABC, abstractmethod

from project_0.bank_account_package.bank_account import BankAccount


class BankAccountAbs(ABC):

    @abstractmethod
    def create_bank_account(self, bank_account: BankAccount):
        pass

    @abstractmethod
    def get_bank_account_info(self, bank_account_num: int):
        pass

    @abstractmethod
    def update_bank_account_info(self, bank_account: BankAccount):
        pass

    @abstractmethod
    def delete_bank_account_info(self, bank_account_num: int):
        pass