from project_0.customer_package.customer import Customer
from project_0.customer_package.customer_abstract import CustomerAbs


class CustomerImp(CustomerAbs):
    customer_ex = Customer("Some", "Customer", 2, 0)
    customer_list = [customer_ex]
    id_for_now = 0

    def create_customer(self, customer: Customer):
        customer.customer_id = CustomerImp.id_for_now
        CustomerImp.id_for_now += 1
        CustomerImp.customer_list.append(customer)
        return customer

    def get_customer_info(self, customer_id: int):
        for customer in CustomerImp.customer_list:
            if customer.customer_id == customer_id:
                return customer

    def update_customer_info(self, customer: Customer):
        for customer_in_list in CustomerImp.customer_list:
            if customer_in_list.customer_id == customer.customer_id:
                index = CustomerImp.customer_list.index(customer_in_list)
                CustomerImp.customer_list[index] = customer
                return customer


    def delete_customer_info(self, customer_id: int):
        for customer_in_list in CustomerImp.customer_list:
            if customer_in_list.customer_id == customer_id:
                index = CustomerImp.customer_list.index(customer_in_list)
                del CustomerImp.customer_list[index]
                return bool
