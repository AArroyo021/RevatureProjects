from datetime import date

from project_1.reimbursements_package.reimbursement import Reimbursement
from three_tiered_webapp_example.util.database_connection import connection


class ReimbursementPostImp():

    def create_reimbursement(self, reimbursement: Reimbursement):
        sql = "insert into reimbursements values(default, %s, %s, %s, NULL, NULL, NULL, %s, NULL) returning claim_num"
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.employee_id, reimbursement.claim_amount, reimbursement.claim_reason, date.today()))
        connection.commit()
        reimbursement_num = cursor.fetchone()[0]
        reimbursement.claim_num = reimbursement_num
        return reimbursement

    def get_reimbursement_info(self, claim_num: int):
        sql = "select * from reimbursements where claim_num = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [claim_num])
        reimbursement_record = cursor.fetchone()
        reimbursement = Reimbursement(*reimbursement_record)
        return reimbursement

    def update_reimbursement_info(self, reimbursement: Reimbursement):
        sql = "update reimbursements set claim_status = %s, manager_validation = %s, manager_reasoning = %s, date_validated = %s where claim_num = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.claim_status, reimbursement.manager_validation, reimbursement.manager_reasoning, date.today(), reimbursement.claim_num))
        connection.commit()
        return reimbursement
