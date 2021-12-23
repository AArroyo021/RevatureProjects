from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Project1HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_username_input(self):
        element: WebElement = self.driver.find_element(By.ID, "usernameInput")
        return element

    def select_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "passwordInput")
        return element

    def select_manager_radio(self):
        element: WebElement = self.driver.find_element(By.ID, "managerRadio")
        return element

    def select_login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "getData")
        return element

    def select_pending_button(self):
        element: WebElement = self.driver.find_element(By.ID, "pendingTab")
        return element

    def select_completed_button(self):
        element: WebElement = self.driver.find_element(By.ID, "completedTab")
        return element

    def select_statistics_button(self):
        element: WebElement = self.driver.find_element(By.ID, "statisticsTab")
        return element

    def select_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logout")
        return element

    def select_claimNum_button(self):
        element: WebElement = self.driver.find_element(By.ID, "claimNum8")
        return element

    def select_claim_approve_status_radio(self):
        element: WebElement = self.driver.find_element(By.ID, "statusARadio")
        return element

    def select_manager_validation_approve_radio(self):
        element: WebElement = self.driver.find_element(By.ID, "managerARadio")
        return element

    def select_manager_reason_input(self):
        element: WebElement = self.driver.find_element(By.ID, "managerRInput")
        return element

    def select_update_button(self):
        element: WebElement = self.driver.find_element(By.ID, "updatePending")
        return element