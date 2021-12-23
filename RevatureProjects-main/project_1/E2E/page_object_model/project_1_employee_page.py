from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Project1HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_username_input(self):
        element: WebElement = self.driver.find_element(By.ID,"usernameInput")
        return element

    def select_password_input(self):
        element: WebElement = self.driver.find_element(By.ID,"passwordInput")
        return element

    def select_login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "getData")
        return element

    def select_create_reimbursement_button(self):
        element: WebElement = self.driver.find_element(By.ID, "pendingTab")
        return element

    def select_reason_input(self):
        element: WebElement = self.driver.find_element(By.ID, "reasonInput")
        return element

    def select_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID," amountInput")
        return element

    def select_create_button(self):
        element: WebElement = self.driver.find_element(By.ID, "getReimbursement")
        return element

    def select_completed_reimbursement_button(self):
        element: WebElement = self.driver.find_element(By.ID, "completedTab")
        return element

    def select_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logout")
        return element