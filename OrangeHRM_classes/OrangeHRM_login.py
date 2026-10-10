import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from OrangeHRM_classes.OrangeHRM_dashboard import Dashboard_section
class Login_section:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.forget_password_button = (By.CLASS_NAME, "orangehrm-login-forgot-header")
        self.reset_password_button = (By.CLASS_NAME, "orangehrm-forgot-password-button--reset")
        self.reset_password_text = (By.XPATH,"//h6[contains(@class,'orangehrm-forgot-password-title')]")

    def login_page(self, user_name, password):
        self.driver.find_element(*self.username).send_keys(user_name)
        self.driver.find_element(*self.password).send_keys(password)
        self.wait.until(expected_conditions.element_to_be_clickable(self.login_button)).click()
        dashboard = Dashboard_section(self.driver)
        return dashboard

    def forgot_password(self, user_name, password):
        self.driver.find_element(*self.username).send_keys(user_name)
        self.driver.find_element(*self.password).send_keys(password)
        self.wait.until(expected_conditions.element_to_be_clickable(self.login_button)).click()
        error_message = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Invalid credentials']"))).text
        print(error_message)
        self.wait.until(expected_conditions.element_to_be_clickable(self.forget_password_button)).click()
        self.driver.find_element(*self.username).send_keys(user_name)
        self.wait.until(expected_conditions.element_to_be_clickable(self.reset_password_button)).click()
        reset_password = self.wait.until(expected_conditions.visibility_of_element_located(self.reset_password_text))
        return reset_password.text







