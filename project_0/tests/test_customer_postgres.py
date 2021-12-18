from project_0.customer_package.customer import Customer
from project_0.customer_package.customer_postgres_imp import CustomerPostgresImp
from project_0.customer_package.customer_postgress_logic import CustomerPostgresLogic

customer_postgres_imp = CustomerPostgresImp()
customer = Customer("FirstTest", "LastTest", 1, 0)
customer_postgres_logic = CustomerPostgresLogic(customer_postgres_imp)
customer_logic = Customer("Logic", "Test", 123, 0)


def test_create_customer():
    new_customer: Customer = customer_postgres_imp.create_customer(customer)
    assert new_customer.customer_id != 0

def test_get_customer_info():
    return_customer: Customer = customer_postgres_imp.get_customer_info(1)
    assert return_customer.customer_id == 1

def test_update_customer_info():
    update_examp = Customer("Example", "Update", 1, 0)
    updated_customer: Customer = customer_postgres_imp.update_customer_info(update_examp)
    assert updated_customer.bank_account == updated_customer.bank_account

def test_delete_customer_info():
    remove_customer = customer_postgres_imp.delete_customer_info(2)
    assert remove_customer

def test_get_all_customers():
    return_all_customers = customer_postgres_imp.get_all_customers()
    assert return_all_customers

"""************************* Logic Tests *******************************************"""

def test_service_create_customer():
    try:
        customer_postgres_logic.service_create_customer(customer_logic)
        assert False
    except Exception as e:
        assert str(e) == "Customer already exists"

