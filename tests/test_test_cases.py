import pytest
import allure

from pages.home_page import Home
from pages.test_cases_page import TestCases
from pages.components.navbar import Navbar
from utils.helpers import Helpers


@allure.story("Test Cases")
class TestTestCases:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home = Home(self.page)
        self.test_cases = TestCases(self.page)
        self.navbar = Navbar(self.page)

    def test_navigation_to_test_cases(self, test_setup):
        """Verify successful navigation to the 'Test Cases' page from the home page.

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        with allure.step("Navigate to the Test Cases page"):
            self.home.check_home_page_visibility()
            self.navbar.click_test_cases_btn()
            Helpers.take_screenshot(self.page, "test_cases_page")

        with allure.step("Check navigation to the Test Cases page"):
            self.test_cases.check_navigation_to_test_cases()
