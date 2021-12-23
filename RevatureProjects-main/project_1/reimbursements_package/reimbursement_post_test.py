from datetime import date

from project_1.reimbursements_package.reimbursement import Reimbursement
from project_1.reimbursements_package.reimbursement_post_imp import ReimbursementPostImp

reimbursement_post_imp = ReimbursementPostImp()
reimbursement = Reimbursement(0, 1, 8947895.32, "I went somewhere", False, False, "N/A", date.today(), date.today())

def test_create_reimbursement():
    new_reimbursement: Reimbursement = reimbursement_post_imp.create_reimbursement(reimbursement)
    assert new_reimbursement.claim_num != 0

def test_get_reimbursement_info():
    return_reimbursement: Reimbursement = reimbursement_post_imp.get_reimbursement_info(1)
    assert return_reimbursement[0].claim_num == 1

def test_get_all_employees_reimbursement_info():
    return_reimbursements: Reimbursement = reimbursement_post_imp.get_all_employees_reimbursement_info(1)
    assert return_reimbursements[0].employee_id == 1

def test_update_reimbursement_info():
    update_status = True
    update_validation = True
    update_reasoning = "Just felt like accepting"
    claim_number = 16
    updated_reimbursement = reimbursement_post_imp.update_reimbursement_info(update_status, update_validation, update_reasoning, claim_number)
    assert updated_reimbursement == claim_number

def test_get_all_reimbursements_info():
    all_reimbursements: Reimbursement = reimbursement_post_imp.get_all_reimbursements_info()
    assert all_reimbursements

def test_get_max_statistics():
    reimb_max: Reimbursement = reimbursement_post_imp.get_max_statistics()
    print(reimb_max)
    assert reimb_max == 8947895.32

def test_get_min_statistics():
    reim_min: Reimbursement = reimbursement_post_imp.get_min_statistics()
    print(reim_min)
    assert reim_min != 0

def test_get_avg_statistics():
    reimb_avg: Reimbursement = reimbursement_post_imp.get_avg_statistics()
    print(reimb_avg)
    assert reimb_avg != 0

def test_get_count_statistics():
    reimb_count: Reimbursement = reimbursement_post_imp.get_count_statistics()
    print(reimb_count)
    assert reimb_count