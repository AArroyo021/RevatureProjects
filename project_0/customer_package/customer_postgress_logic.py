from project_0.customer_package.customer import Customer
from project_0.customer_package.customer_postgres_imp import CustomerPostgresImp


class CustomerPostgresLogic():
    def __init__(self, customer_postgres):
        self.customer_postgres: CustomerPostgresImp = customer_postgres

    def service_create_customer(self, customer: Customer):
        for current_customer in self.customer_postgres.customer_list:
            if current_customer.customer_id == customer.customer_id:
                raise Exception("Customer already exists")
        else:
            return self.customer_postgres.create_customer(customer)

    def service_get_customer_info(self, customer_id: int):
        return self.customer_postgres.get_customer_info(customer_id)

    def service_update_customer_info(self, customer: Customer):
        return self.customer_postgres.update_customer_info(customer)

    def service_delete_customer_info(self, customer_id: int):
        return self.customer_postgres.delete_customer_info(customer_id)

    def service_get_all_customers(self):
        return self.customer_postgres.get_all_customers()