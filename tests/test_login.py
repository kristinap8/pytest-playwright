import pytest
import allure

from pages.home_page import Home
from pages.login_page import Login
from pages.delete_account_page import DeleteAccount
from pages.signup_page import Signup
from pages.account_created_page import AccountCreated
from pages.components.navbar import Navbar
from utils.helpers import Helpers
from utils.data_generator import DataGenerator


@allure.story("Login")
class TestLogin:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home = Home(self.page)
        self.login = Login(self.page)
        self.signup = Signup(self.page)
        self.delete_account = DeleteAccount(self.page)
        self.account_created = AccountCreated(self.page)
        self.navbar = Navbar(self.page)
        self.data_generator = DataGenerator()

        return self

    def test_login_with_valid_credentials(self, test_setup):
        """Test the login process with correct email and password.

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

        with allure.step("Delete account and verify success message"):
            self.navbar.click_delete_account_btn()
            Helpers.take_screenshot(self.page, "delete_account_page")
            self.delete_account.check_msg_title_visibility()
            Helpers.take_screenshot(self.page, "delete_account_message")

    def test_login_with_incorrect_credentials(self, test_setup):
        """Test the login process by attempting to log in with incorrect email and password.

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        with allure.step("Navigate to the Signup/Login page"):
            self.home.check_home_page_visibility()
            self.navbar.click_signup_login_btn()
            Helpers.take_screenshot(self.page, "sign_up/login_page")

        with allure.step("Login with incorrect credentials"):
            self.login.check_login_form_title_visibility()
            self.login.login(self.data_generator.generate_email(), self.data_generator.generate_password())
            Helpers.take_screenshot(self.page, "filled_login_form")

        with allure.step("Verify login error message"):
            self.login.check_login_error_msg_visibility()
            Helpers.take_screenshot(self.page, "login_error_message")

