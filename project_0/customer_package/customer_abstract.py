from abc import ABC, abstractmethod

from project_0.customer_package.customer import Customer


class CustomerAbs(ABC):

    @abstractmethod
    def create_customer(self, customer: Customer):
        pass

    @abstractmethod
    def get_customer_info(self, customer_id: int):
        pass

    @abstractmethod
    def update_customer_info(self, customer: Customer):
        pass

    @abstractmethod
    def delete_customer_info(self, customer_id: int):
        pass

    @abstractmethod
    def get_all_customers(self):
        pass