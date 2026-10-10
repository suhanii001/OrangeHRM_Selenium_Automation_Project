import pytest
import json

from OrangeHRM_classes.OrangeHRM_login import Login_section
data_path = "OrangeHRM_Jsonfiles/OrangeHRM_login_data.json"
with open(data_path) as f:
    data = json.load(f)
    details = data["details"]
employee_path = "OrangeHRM_Jsonfiles/OrangeHRM_employee_details.json"
with open(employee_path) as f:
    employee_data = json.load(f)
    employees_details = employee_data["details"]

@pytest.mark.parametrize("details_data", details)
def test_login_page_check(browser_requested, details_data):
    driver = browser_requested
    login = Login_section(driver)
    if details_data["user_name"] == "Laila":
        message = login.forgot_password(details_data["user_name"], details_data["password"])
        assert message == "Invalid user", "Reset Password link sent successfully"
    else:
        login.login_page(details_data["user_name"], details_data["password"])

def test_dashboard_page_check(browser_requested):
    driver = browser_requested
    login = Login_section(driver)
    dashboard = login.login_page("Admin", "admin123")
    dashboard.dashboard_options()
    dashboard.PIM_click()
@pytest.mark.smoke
@pytest.mark.parametrize("employees_input", employees_details)
def test_PIM_page_check(browser_requested, employees_input):
    driver = browser_requested
    login = Login_section(driver)
    dashboard = login.login_page("Admin", "admin123")
    pim_obj = dashboard.PIM_click()
    pim_obj.add_employee(employees_input["first_name"], employees_input["last_name"], employees_input["username"], employees_input["password"], employees_input["confirm_password"])
    final_message = pim_obj.search_employee(employees_input["first_name"], employees_input["last_name"])
    assert "1" in final_message, "Employee still exists after deletion"
    print(final_message)









