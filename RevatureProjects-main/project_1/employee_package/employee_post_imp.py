from project_1.employee_package.employee import Employee
from util.database_connection import connection


class EmployeePostImp():

    def get_employee_login(self, employee_username: str):
        sql = "select * from employee where employee_username = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_username])
        employee_record = cursor.fetchone()
        employee = Employee(*employee_record)
        return employee

#********************************************** Logic Implementation *********************************************

    def employee_login_check(self, username_input: str, password_input: str):
        current_employee = self.get_employee_login(username_input)
        if current_employee.employee_username == username_input:
            if current_employee.employee_password == password_input:
                return True, current_employee.employee_id
        raise Exception("Incorrect username or password")