from datetime import date

from project_1.reimbursements_package.reimbursement import Reimbursement
from util.database_connection import connection


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
        reimbursement_record = cursor.fetchall()
        reimburs_list = []
        for reimbursement in reimbursement_record:
            reimburs_list.append(Reimbursement(*reimbursement))
        return reimburs_list

    def get_all_employees_reimbursement_info(self, employee_id: int):
        sql = "select * from reimbursements where employee_Id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        reimbursement_record = cursor.fetchall()
        reimburs_list = []
        for reimbursement in reimbursement_record:
            reimburs_list.append(Reimbursement(*reimbursement))
        return reimburs_list

    def update_reimbursement_info(self, claim_status: bool, manager_validation: bool, manager_reasoning: str, claim_num: int):
        sql = "update reimbursements set claim_status = %s, manager_validation = %s, manager_reasoning = %s, date_validated = %s where claim_num = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (claim_status, manager_validation, manager_reasoning, date.today(), claim_num))
        connection.commit()
        return claim_num

    def get_all_reimbursements_info(self):
        sql = "select * from reimbursements"
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_record = cursor.fetchall()
        reimburs_list = []
        for reimbursement in reimbursement_record:
            reimburs_list.append(Reimbursement(*reimbursement))
        return reimburs_list

    def get_max_statistics(self):
        sqlMax = "select max(claim_amount) from reimbursements"
        cursor = connection.cursor()
        cursor.execute(sqlMax)
        max_record = cursor.fetchone()[0]
        return max_record

    def get_min_statistics(self):
        sqlMin = "select min(claim_amount) from reimbursements"
        cursor = connection.cursor()
        cursor.execute(sqlMin)
        min_record = cursor.fetchone()[0]
        return min_record

    def get_avg_statistics(self):
        sqlAvg = "select avg(claim_amount) from reimbursements"
        cursor = connection.cursor()
        cursor.execute(sqlAvg)
        avg_record = cursor.fetchone()[0]
        return avg_record

    def get_count_statistics(self):
        sqlCount = "select employee_id, count(employee_id) from reimbursements group by employee_id"
        cursor = connection.cursor()
        cursor.execute(sqlCount)
        count_record = cursor.fetchall()
        return count_record