from flask import Flask, jsonify, request

from project_0.bank_account_package.bank_account import BankAccount
from project_0.bank_account_package.bank_account_logic import BankAccountLogic
from project_0.bank_account_package.bank_account_postgres_imp import BankAccountPostgresImp
from project_0.customer_package.customer import Customer
from project_0.customer_package.customer_postgres_imp import CustomerPostgresImp
from project_0.customer_package.customer_postgress_logic import CustomerPostgresLogic
import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)

customer_postgres_imp = CustomerPostgresImp()
customer_postgres_logic = CustomerPostgresLogic(customer_postgres_imp)
bank_postgres_imp = BankAccountPostgresImp()
bank_postgres_logic = BankAccountLogic(bank_postgres_imp)

#create customer
@app.post("/customer")
def create_customer_entry():
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["bankAccount"],
            customer_data["customerId"]
         )
        customer_to_return = customer_postgres_logic.service_create_customer(new_customer)
        customer_as_dictionary = customer_to_return.make_person_dictionary()
        customer_as_json = jsonify(customer_as_dictionary)
        return customer_as_json
    except Exception as e:
        exception_dictionary = {"Message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json

#get customer info
@app.get("/customer/info/<customer_id>")
def get_customer_info(customer_id):
    try:
        customer_information = customer_postgres_logic.service_get_customer_info(int(customer_id))
        customer_dictionary = customer_information.make_person_dictionary()
        customer_info_json = jsonify(customer_dictionary)
        return customer_info_json
    except AttributeError as e:
        return jsonify("No customer information available")

#update customer info
@app.patch("/customer/info/<customer_id>")
def update_customer_info(customer_id: str):
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["bankAccount"],
            int(customer_id)
        )
        updated_customer = customer_postgres_logic.service_update_customer_info(new_customer)
        return "Customer updated successfully, the player info is now " + str(updated_customer)
    except Exception as e:
        exception_dictionary = {"Message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json

#delete customer info
@app.delete("/customer/info/<customer_id>")
def delete_customer_info(customer_id: str):
    result = customer_postgres_logic.service_delete_customer_info(int(customer_id))
    if result:
        return "Customer with id {} was deleted successfully".format(customer_id)
    else:
        return "Something went wrong: customer with id {} was not deleted".format(customer_id)

@app.get("/customer/info")
def get_all_customers_info():
    all_customers = customer_postgres_logic.service_get_all_customers()
    customers_as_dictionary = []
    for customers in all_customers:
        customer_dict = customers.make_person_dictionary()
        customers_as_dictionary.append(customer_dict)
    return jsonify(customers_as_dictionary)

"""
********************************************* Bank Accounts **************************************************************************
"""

@app.post("/account")
def create_bank_account_entry():
    try:
        bank_data = request.get_json()
        new_bank = BankAccount(
            bank_data["balance"],
            bank_data["bankAccountNum"],
            bank_data["customerId"]
        )
        bank_returned = bank_postgres_logic.service_create_bank_account(new_bank)
        bank_dict = bank_returned.make_bank_account_dictionary()
        bank_dict_as_json = jsonify(bank_dict)
        return bank_dict_as_json
    except Exception as e:
        exception_dictionary = {"Message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json

@app.get("/account/<bankAccountNum>")
def get_bank_account_info(bankAccountNum: int):
    bank_info = bank_postgres_logic.service_get_bank_account_info(int(bankAccountNum))
    bank_dict = bank_info.make_bank_account_dictionary()
    get_json = jsonify(bank_dict)
    return get_json

@app.patch("/account/<bankAccountNum>")
def update_bank_account_info(bankAccountNum: str):
    bank_data = request.get_json()
    new_info = BankAccount(
        bank_data["balance"],
        int(bankAccountNum),
        bank_data["customerId"]
    )
    returned_info = bank_postgres_logic.service_update_bank_account_info(new_info)
    info_as_dict = returned_info.make_bank_account_dictionary()
    dict_as_json = jsonify(info_as_dict)
    return dict_as_json

@app.delete("/account/<bankAccountNum>")
def delete_bank_account_info(bankAccountNum):
    result = bank_postgres_logic.service_delete_bank_account_info(bankAccountNum)
    if result:
        return "Bank Account with id {} was deleted successfully".format(bankAccountNum)
    else:
        return "Something went wrong: bank account with id {} was not deleted".format(bankAccountNum)

@app.patch("/account/transfer")
def transfer_into_bank_account():
    try:
        data = request.get_json()
        transfer_amount = data["transferAmount"]
        transfer_account = data["transferAccount"]
        receive_account = data["receiveAccount"]
        bank_postgres_logic.service_transfer_funds_between_accounts(int(transfer_amount), int(transfer_account), int(receive_account))
        return " ${} amount was transferred from Account: {} to Account: {}.".format(transfer_amount, transfer_account, receive_account)
    except Exception as e:
        error = {"Message": str(e)}
        return error

@app.patch("/account/withdraw/<bankAccountNum>")
def withdraw_from_account(bankAccountNum: int):
    try:
        bank_data = request.get_json()
        amount = bank_data["withdrawAmount"]
        int(bankAccountNum)
        bank_postgres_logic.service_account_withdrawal(int(amount), bankAccountNum)
        return "You have withdrawn {}".format(amount)
    except Exception as e:
        error_message = {"Message": str(e)}
        return jsonify(error_message)

@app.patch("/account/deposit/<bankAccountNum>")
def deposit_from_account(bankAccountNum: int):
    try:
        bank_data = request.get_json()
        amount = bank_data["depositAmount"]
        int(bankAccountNum)
        bank_postgres_logic.service_account_deposit(int(amount), bankAccountNum)
        return "You have deposited {}".format(amount)
    except Exception as e:
        error_message = {"Message": str(e)}
        return jsonify(error_message)

@app.get("/account/customer/<customerId>")
def get_all_accounts_from_customer(customer_id):
    all_accounts = bank_postgres_logic.service_get_all_accounts_from_customer(int(customer_id))
    accounts_as_dict = []
    for accounts in all_accounts:
        account_dict = accounts.make_bank_account_dictionary()
        accounts_as_dict.append(account_dict)
    return jsonify(accounts_as_dict)


app.run()
