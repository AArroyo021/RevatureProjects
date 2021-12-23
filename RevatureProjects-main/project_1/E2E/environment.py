from behave.runner import Context
from selenium import webdriver
from page_object_model.project_1_employee_page import Project1HomePage
from page_object_model.project_1_manager_page import Project1HomePage


def before_all(context: Context):
    context.driver = webdriver.Chrome("project_1/E2E/chromedriver.exe")
    context.project_1_page = Project1HomePage(context.driver)
    context.driver.implicitly_wait(4)


def after_all(context: Context):
    context.driver.quit()