class Manager:
    def __init__(self, manager_username: str, manager_password: str, manager_id: int):
        self.manager_username = manager_username
        self.manager_password = manager_password
        self.manager_id = manager_id

    def make_employee_dictionary(self):
        return {
            "managerUsername": self.manager_username,
            "managerPassword": self.manager_password,
            "managerId": self.manager_id
        }