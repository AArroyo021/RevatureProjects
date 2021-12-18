class Employee:
    def __init__(self, employee_username: str, employee_password: str, employee_id: int):
        self.employee_username = employee_username
        self.employee_password = employee_password
        self.employee_id = employee_id

    def make_employee_dictionary(self):
        return {
            "employeeUsername": self.employee_username,
            "employeePassword": self.employee_password,
            "employeeId": self.employee_id
        }