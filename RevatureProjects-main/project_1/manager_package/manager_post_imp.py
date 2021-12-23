from project_1.manager_package.manager import Manager
from util.database_connection import connection


class ManagerPostImp():

    def get_manager_login(self, manager_username: str):
        sql = "select * from manager where manager_username = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [manager_username])
        manager_record = cursor.fetchone()
        manager = Manager(*manager_record)
        return manager

#********************************************** Logic Implementation *********************************************

    def manager_login_check(self, username_input: str, password_input: str):
        current_manager = self.get_manager_login(username_input)
        if current_manager.manager_username == username_input:
            if current_manager.manager_password == password_input:
                return True, current_manager.manager_id
        raise Exception("Incorrect username or password")