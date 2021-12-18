from datetime import date

from project_1.reimbursements_package.reimbursement import Reimbursement
from project_1.reimbursements_package.reimbursement_post_imp import ReimbursementPostImp

reimbursement_post_imp = ReimbursementPostImp()
reimbursement = Reimbursement(0, 1, 100.32, "I was hungry", False, False, "N/A", date.today(), date.today())

def test_create_reimbursement():
    new_reimbursement: Reimbursement = reimbursement_post_imp.create_reimbursement(reimbursement)
    assert new_reimbursement.claim_num != 0

def test_get_reimbursement_info():
    return_reimbursement: Reimbursement = reimbursement_post_imp.get_reimbursement_info(1)
    assert return_reimbursement.claim_num == 1

def test_update_reimbursement_info():
    update_examp = Reimbursement(2, 1, 100.32, "I was hungry", True, True, "He was hungry", date.today(), date.today())
    updated_reimbursement = reimbursement_post_imp.update_reimbursement_info(update_examp)
    assert updated_reimbursement.claim_num == updated_reimbursement.claim_num
