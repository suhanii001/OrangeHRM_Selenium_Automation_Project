
# OrangeHRM Selenium Automation Framework

## Project Overview
This project automates selected OrangeHRM web application scenarios using Python, Selenium WebDriver, and PyTest, POM.

## Technologies Used
- Python
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- JSON test data
- PyTest HTML reporting
- Pytest Parallel Execution

## Project Structure
- `OrangeHRM_classes/` - Page classes and reusable automation methods
- `OrangeHRM_Jsonfiles/` - Test data in JSON format
- `test_orangeHRM.py` - Test cases
- `conftest.py` - Shared PyTest fixtures and configuration
- `pytest.ini` - PyTest configuration
- `assets/` - Supporting project files

## Prerequisites
- Python 3
- Various browser supported by the framework
- Required Python packages listed in `requirements.txt`

## Installation
1. Clone this repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   `python -m pip install -r requirements.txt`

## Run Tests
Run the tests from the project root:

`python -m pytest -v`

## Reports
The project may generate HTML reports or screenshots locally, depending on the test configuration.
