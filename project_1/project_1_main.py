from flask import Flask, jsonify, request
from flask_cors import CORS

from project_1.employee_package.employee_post_imp import EmployeePostImp
from project_1.reimbursements_package.reimbursement import Reimbursement
from project_1.reimbursements_package.reimbursement_post_imp import ReimbursementPostImp

app: Flask = Flask(__name__)
CORS(app)

employee_post_imp = EmployeePostImp()
reimbursement_post_imp = ReimbursementPostImp()

@app.post("/login/employee")
def employee_login():
    try:
        login_data = request.get_json()
        username_input = login_data["employeeUsername"]
        password_input = login_data["employeePassword"]
        login_check = employee_post_imp.employee_login_check(username_input, password_input)
        login_json = jsonify(login_check)
        return login_json, 200
    except Exception as e:
        return jsonify("Login Failed: Username or Password is incorrect")

@app.post("/employee/reimbursement")
def employee_reimbursement_request():
    try:
        reimb_data = request.get_json()
        new_reimb = Reimbursement(
            reimb_data["claimNum"],
            reimb_data["employeeId"],
            reimb_data["claimAmount"],
            reimb_data["claimReason"],
            reimb_data["claimStatus"],
            reimb_data["managerValidation"],
            reimb_data["managerReasoning"],
            reimb_data["dateSent"],
            reimb_data["dateValidated"]
        )
        create_reimb = reimbursement_post_imp.create_reimbursement(new_reimb)
        reimb_as_dict = create_reimb.make_reimbursement_dict()
        reimb_as_json = jsonify(reimb_as_dict)
        return reimb_as_json
    except Exception as e:
        except_dict = {"Message": str(e)}
        except_json = jsonify(except_dict)
        return except_json

app.run()