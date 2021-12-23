from flask import Flask, jsonify, request
from flask_cors import CORS

from project_1.employee_package.employee_post_imp import EmployeePostImp
from project_1.manager_package.manager_post_imp import ManagerPostImp
from project_1.reimbursements_package.reimbursement import Reimbursement
from project_1.reimbursements_package.reimbursement_post_imp import ReimbursementPostImp
import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)
CORS(app)

employee_post_imp = EmployeePostImp()
reimbursement_post_imp = ReimbursementPostImp()
manager_post_imp = ManagerPostImp()

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
        return reimb_as_json, 200
    except Exception as e:
        except_dict = {"Message": str(e)}
        except_json = jsonify(except_dict)
        return except_json

@app.post("/employee/reimbursement/info")
def get_reimbursement_info():
    try:
        data = request.get_json()
        claim_num = data["claimNum"]
        all_reimbursement = reimbursement_post_imp.get_reimbursement_info(claim_num)
        reimbursement_as_dict = []
        for reimbursements in all_reimbursement:
            reimb_dict = reimbursements.make_reimbursement_dict()
            reimbursement_as_dict.append(reimb_dict)
        return jsonify(reimbursement_as_dict)
    except AttributeError as e:
        return jsonify("No reimbursement information available")

@app.post("/employee/reimbursements")
def get_all_employee_reimbursement_info():
    try:
        data = request.get_json()
        employee_id = data["employeeId"]
        all_reimbursement = reimbursement_post_imp.get_all_employees_reimbursement_info(employee_id)
        reimbursement_as_dict = []
        for reimbursements in all_reimbursement:
            reimb_dict = reimbursements.make_reimbursement_dict()
            reimbursement_as_dict.append(reimb_dict)
        return jsonify(reimbursement_as_dict)
    except AttributeError as e:
        return jsonify("No reimbursement information available")

@app.patch("/manager/reimbursements")
def update_reimbursement_request():
    try:
        data = request.get_json()
        claim_status = data["claimStatus"]
        manager_validation = data["managerValidation"]
        manager_reasoning = data["managerReasoning"]
        claim_num = data["claimNum"]
        update_reimb = reimbursement_post_imp.update_reimbursement_info(claim_status, manager_validation, manager_reasoning, claim_num)
        reimb_info = reimbursement_post_imp.get_reimbursement_info(update_reimb)
        reimbursement_dict = []
        for reimbursements in reimb_info:
            reimb_dict = reimbursements.make_reimbursement_dict()
            reimbursement_dict.append(reimb_dict)
            return jsonify(reimbursement_dict)
    except Exception as e:
        return jsonify("Reimbursement update failed")

@app.post("/login/manager")
def manager_login():
    try:
        login_data = request.get_json()
        username_input = login_data["managerUsername"]
        password_input = login_data["managerPassword"]
        login_check = manager_post_imp.manager_login_check(username_input, password_input)
        login_json = jsonify(login_check)
        return login_json, 200
    except Exception as e:
        return jsonify("Login Failed: Username or Password is incorrect")

@app.get("/manager/reimbursements/info")
def get_all_reimbursement_info():
    try:
        all_reimbursements = reimbursement_post_imp.get_all_reimbursements_info()
        reimbursement_as_dict = []
        for reimbursements in all_reimbursements:
            reimb_dict = reimbursements.make_reimbursement_dict()
            reimbursement_as_dict.append(reimb_dict)
        return jsonify(reimbursement_as_dict)
    except Exception as e:
        return jsonify("No reimbursement information available")

@app.get("/manager/reimbursements/stats")
def get_all_stats_info():
    try:
        maxAmount = reimbursement_post_imp.get_max_statistics()
        minAmount = reimbursement_post_imp.get_min_statistics()
        avgAmount = reimbursement_post_imp.get_avg_statistics()
        countStats = reimbursement_post_imp.get_count_statistics()
        statistics_dict = {"max": maxAmount, "min": minAmount, "avg": avgAmount, "count": countStats}
        return jsonify(statistics_dict)
    except Exception as e:
        return jsonify("Stats couldn't get sent over")



app.run()