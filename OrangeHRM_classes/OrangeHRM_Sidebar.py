
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from OrangeHRM_classes.OrangeHRM_PIM import PIM_section

class Navigation_sidebar_section:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.length_of_list = (By.CSS_SELECTOR, "ul[class='oxd-main-menu'] li")
        self.menu_options = (By.CSS_SELECTOR, "ul[class='oxd-main-menu'] li")
        self.PIM_option = (By.XPATH, "//span[normalize-space()='PIM']")

    def sidebar_options(self):
        options_list = len(self.driver.find_elements(*self.length_of_list))
        for o in range(options_list):
            menu_list = self.driver.find_elements(*self.menu_options)
            if menu_list[o].text == "Maintenance":
                continue
            else:
                print("Option which is clicked is:", menu_list[o].text)
                self.wait.until(expected_conditions.element_to_be_clickable(menu_list[o])).click()


    def PIM_click(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.PIM_option)).click()
        pim_obj = PIM_section(self.driver)
        return pim_obj




