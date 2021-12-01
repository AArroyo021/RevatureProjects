from project_0.customer_package.customer import Customer
from project_0.customer_package.customer_imp import CustomerImp

customer_imp = CustomerImp()
customer = Customer("FirstTest", "LastTest", 1, 0)

def test_create_customer():
    new_customer: Customer = customer_imp.create_customer(customer)
    assert new_customer.customer_id != 1

def test_get_customer_info():
    return_customer: Customer = customer_imp.get_customer_info(0)
    assert return_customer.customer_id == 0

def test_update_customer_info():
    update_examp = Customer("Example", "Update", 1,0)
    updated_customer: Customer = customer_imp.update_customer_info(update_examp)
    assert updated_customer.bank_account == updated_customer.bank_account

def test_delete_customer_info():
    remove_customer = customer_imp.delete_customer_info(0)
    assert remove_customer
