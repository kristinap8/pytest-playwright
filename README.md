# Automation Exercise -- testing using Playwright + Pytest

This repository contains automated tests for the [Automation Exercise](https://automationexercise.com/) website using the pytest + playwright testing framework. The implemented test cases corresponds to the first 10 test cases available on the [Test cases](https://automationexercise.com/test_cases) page of the Automation Exercise website. <br>
The Allure report generated from the test runs is deployed to [GitHub Pages](https://kristinap8.github.io/pytest-playwright/). <br>
GitHub Actions workflow runs include a Slack notification providing the status of the job run and a link to the deployed Allure report.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Generating Allure Report](#generating-allure-report)

## Requirements

- Python (version 3.x)
- IDE: PyCharm or other Python-compatible IDE
- Pip
- Pipenv

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kristinap8/pytest-playwright.git
   cd pytest-playwright
   ```

2. Set up the environment:

    ```bash
   python -m pip install --upgrade pip
   pip install pipenv
   pipenv install --system
   playwright install
   ```

## Run tests

1. To run tests in the Chrome browser in headless mode using 2 workers, execute the following command:

    ```bash
    pytest
    ```

2. Choose a different browser by specifying the --browser_name flag. Supported options are chromium, firefox, and webkit:

    ```bash
    pytest --browser_name=chromium
    pytest --browser_name=firefox
    pytest --browser_name=webkit
    ```

3. By default, tests run in headless mode. To run tests in headed mode, set the --headed flag:

    ```bash
    pytest --headed
    ```

4. To run specific tests, use the -k flag and provide a test name:

    ```bash
    pytest -k <name of the test>
    ```

5. To run tests in parallel, use the -n flag with the desired number of workers. By default, it is set to 2 workers. For automatic parallelism, set it to "auto" or specify the number of workers:

    ```bash
    pytest -n <number of workers>
    ```

## Generate allure report:
 
Allure reports are generated after each test run. To view the generated Allure report, execute the following command:

    ```bash
    allure serve reports
    ```

