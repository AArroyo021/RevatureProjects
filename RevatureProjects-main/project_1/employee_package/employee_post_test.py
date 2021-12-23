from project_1.employee_package.employee_post_imp import EmployeePostImp

employee_post_imp = EmployeePostImp()
username_input = 'Employee1'
password_input = 'PasswordABC'

def test_get_employee_login():
    return_employee_login = employee_post_imp.get_employee_login('Employee1')
    assert return_employee_login.employee_username == 'Employee1'

def test_employee_login_check():
    try:
        employee_post_imp.employee_login_check(username_input, password_input)
        print("Worked")
        assert True
    except Exception as e:
        print("No work")
        assert str(e) == "Incorrect username or password"