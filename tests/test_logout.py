import pytest
import allure
from playwright.sync_api import expect
import re

from pages.home_page import Home
from pages.login_page import Login
from pages.signup_page import Signup
from pages.account_created_page import AccountCreated
from pages.components.navbar import Navbar
from utils.data_generator import DataGenerator
from utils.helpers import Helpers


@allure.story("Logout")
class TestLogout:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home = Home(self.page)
        self.login = Login(self.page)
        self.signup = Signup(self.page)
        self.account_created = AccountCreated(self.page)
        self.data_generator = DataGenerator()
        self.navbar = Navbar(self.page)

        return self

    def test_logout(self, test_setup):
        """Test the logout process for a logged-in user with valid credentials.

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        with allure.step("Register the user"):
            registered_username, registered_email, registered_password = Helpers.register_user(test_setup)

        with allure.step("Navigate to the Signup/Login page"):
            self.home.check_home_page_visibility()
            self.navbar.click_signup_login_btn()
            Helpers.take_screenshot(self.page, "sign_up/login_page")

        with allure.step("Login with valid credentials"):
            self.login.check_login_form_title_visibility()
            self.login.login(registered_email, registered_password)

        with allure.step(f"Verify that 'Logged in as {registered_username}' is visible"):
            self.navbar.check_logged_in_username_visibility()
            Helpers.take_screenshot(self.page, "logged_in_user")

        with allure.step("Successfully logout"):
            self.navbar.click_logout_btn()
            expect(self.page).to_have_url(re.compile("/login$"))
            Helpers.take_screenshot(self.page, "logout_success")


