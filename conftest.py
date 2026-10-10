import pytest
import os
import pytest_html
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="Firefox", help="browser selection"
    )

@pytest.fixture(scope="function")
def browser_requested(request):

    browser = request.config.getoption("--browser")
    if browser == "Chrome":
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(5)
    elif browser == "Firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    elif browser == "Edge":
        driver = webdriver.Edge()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(5)
    else:
        print("No browser selected")
    yield driver
    driver.quit()

def pytest_sessionfinish(session, exitstatus):
    print("\nProject is completed")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("browser_requested")

        if driver:

            # Create reports folder if it doesn't exist
            reports_dir = os.path.join(os.path.dirname(__file__), "reports")
            os.makedirs(reports_dir, exist_ok=True)

            # Screenshot name
            file_name = (
                report.nodeid
                .replace("::", "_")
                .replace("/", "_")
                .replace("\\", "_")
                .replace("[", "_")
                .replace("]", "")
                + ".png"
            )

            screenshot_path = os.path.join(reports_dir, file_name)

            # Save Screenshot
            driver.save_screenshot(screenshot_path)

            print(f"Screenshot saved at: {screenshot_path}")

            # Attach Screenshot to HTML Report
            extras.append(pytest_html.extras.png(screenshot_path))

    report.extras = extras
