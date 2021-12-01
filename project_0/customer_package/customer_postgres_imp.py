from project_0.customer_package.customer import Customer
from project_0.customer_package.customer_imp import CustomerImp
from three_tiered_webapp_example.util.database_connection import connection


class CustomerPostgresImp(CustomerImp):

    def create_customer(self, customer: Customer):
        sql = "insert into customer values(%s, %s, %s, default) returning customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.bank_account))
        connection.commit()
        customer_id = cursor.fetchone()[0]
        customer.customer_id = customer_id
        return customer

    def get_customer_info(self, customer_id: int):
        sql = "select * from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        customer_record = cursor.fetchone()
        customer = Customer(*customer_record)
        return customer

    def update_customer_info(self, customer: Customer):
        sql = "update customer set first_name = %s, last_name = %s, bank_account = %s where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.bank_account, customer.customer_id))
        connection.commit()
        return customer

    def delete_customer_info(self, customer_id: int):
        sql = "delete from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        return True