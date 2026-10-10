
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PIM_section:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.add_option = (By.CLASS_NAME, "oxd-button-icon")
        self.first_name = (By.NAME, "firstName")
        self.last_name = (By.NAME, "lastName")
        self.invisible_oxd_loader = (By.CLASS_NAME, "oxd-form-loader")
        self.create_login = (By.XPATH, "//span[contains(@class,'oxd-switch-input')]")
        self.username = (By.XPATH, "//label[text()='Username']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        self.password = (By.XPATH, "//input[@type='password']")
        self.confirm_password = (By.XPATH, "//label[text()='Confirm Password']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        self.save_employee = (By.XPATH, "//button[@type='submit']")
        self.invisible_oxd_spinner = (By.CLASS_NAME, "oxd-loading-spinner")
        self.employee_list_option = (By.LINK_TEXT, "Employee List")
        self.search_field = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.search_name_options = (By.XPATH, "//div[@role='option']")
        self.search_employee_name = (By.XPATH, "//button[normalize-space()='Search']")
        self.delete_employee = (By.CLASS_NAME, "bi-trash")
        self.delete_confirmation = (By.XPATH, "//button[normalize-space()='Yes, Delete']")
        self.table_count = (By.CLASS_NAME, "oxd-table-card")
        self.end_message = (By.XPATH, "//span[normalize-space()='(1) Record Found']")

    def add_employee(self, first_name, last_name, username, password, confirm_password):
        self.wait.until(expected_conditions.element_to_be_clickable(self.add_option)).click()
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        print(f"Firstname of the user is: {first_name} and Lastname of the user is: {last_name}")
        self.wait.until(expected_conditions.invisibility_of_element_located(self.invisible_oxd_loader))
        self.wait.until(expected_conditions.element_to_be_clickable(self.create_login)).click()
        self.driver.find_element(*self.username).send_keys(username)
        print("Username of the current user is: ", username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.confirm_password).send_keys(confirm_password)
        print(f"Password of the current user is:  {password}, and confirmation password is:  {confirm_password}")
        self.wait.until(expected_conditions.element_to_be_clickable(self.save_employee)).click()
        self.wait.until(expected_conditions.invisibility_of_element_located(self.invisible_oxd_spinner))

    def search_employee(self, first_name, last_name):
        self.wait.until(expected_conditions.element_to_be_clickable(self.employee_list_option)).click()
        self.driver.find_element(*self.search_field).send_keys(first_name)
        self.wait.until(expected_conditions.visibility_of_all_elements_located(self.search_name_options))
        time.sleep(2)
        expected_name = f"{first_name} {last_name}"
        list_box = self.driver.find_elements(*self.search_name_options)
        for l in list_box:
            print("Employee name Options: ", l.text)
            if l.text.strip() == expected_name:
                print("Selected employee: ", l.text)
                l.click()
                break
        self.wait.until(expected_conditions.element_to_be_clickable(self.search_employee_name)).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.wait.until(expected_conditions.invisibility_of_element_located(self.invisible_oxd_spinner))
        self.wait.until(expected_conditions.element_to_be_clickable(self.delete_employee)).click()
        self.wait.until(expected_conditions.element_to_be_clickable(self.delete_confirmation)).click()
        self.wait.until(expected_conditions.invisibility_of_element_located(self.invisible_oxd_spinner))
        message = self.wait.until(expected_conditions.visibility_of_element_located(self.end_message)).text
        return message
        






