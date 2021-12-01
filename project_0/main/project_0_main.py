from flask import Flask, jsonify, request

from project_0.customer_package.customer import Customer
from project_0.customer_package.customer_imp import CustomerImp

app: Flask = Flask(__name__)

customer_imp = CustomerImp()

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
        customer_to_return = customer_imp.create_customer(new_customer)
        customer_as_dictionary = customer_to_return.make_person_dictionary()
        customer_as_json = jsonify(customer_as_dictionary)
        return customer_as_json
    except Exception as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json

#get customer info
@app.get("/customer/info/<customer_id>")
def get_customer_info(customer_id):
    try:
        customer_information = customer_imp.get_customer_info(int(customer_id))
        customer_dictionary = customer_information.make_person_dictionary()
        customer_info_json = jsonify(customer_dictionary)
        return customer_info_json
    except AttributeError as e:
        return jsonify("No player information available")

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
        updated_customer = customer_imp.update_customer_info(new_customer)
        return "Customer updated successfully, the player info is now " + str(updated_customer)
    except Exception as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json

#delete customer info
@app.delete("/customer/info/<customer_id>")
def delete_customer_info(customer_id: str):
    result = customer_imp.delete_customer_info(int(customer_id))
    if result:
        return "Customer with id {} was deleted successfully".format(customer_id)
    else:
        return "Something went wrong: customer with id {} was not deleted".format(customer_id)


app.run()
