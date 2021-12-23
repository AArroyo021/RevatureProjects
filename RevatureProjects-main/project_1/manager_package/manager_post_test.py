from project_1.manager_package.manager_post_imp import ManagerPostImp

manager_post_imp = ManagerPostImp()
username_input = "Manager1"
password_input = "Pass1"

def test_get_manager_login():
    return_manager_login = manager_post_imp.get_manager_login(username_input)
    assert return_manager_login.manager_username == username_input

def test_manager_login_check():
    try:
        manager_post_imp.manager_login_check(username_input, password_input)
        assert True
    except Exception as e:
        assert str(e) == "Incorrect username or password"