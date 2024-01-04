import pytest
import allure

from pages.home_page import Home
from pages.login_page import Login
from pages.signup_page import Signup
from pages.account_created_page import AccountCreated
from pages.delete_account_page import DeleteAccount
from pages.components.navbar import Navbar
from utils.helpers import Helpers
from utils.data_generator import DataGenerator


@allure.story("Registration")
class TestRegistration:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home = Home(self.page)
        self.login = Login(self.page)
        self.signup = Signup(self.page)
        self.account_created = AccountCreated(self.page)
        self.delete_account = DeleteAccount(self.page)
        self.navbar = Navbar(self.page)
        self.data_generator = DataGenerator()

        return self

    def test_registration_with_valid_credentials(self, test_setup):
        """Test the registration process by signing up a new user with valid credentials.

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        with allure.step("Navigate to the Signup/Login page"):
            self.home.check_home_page_visibility()
            self.navbar.click_signup_login_btn()
            Helpers.take_screenshot(self.page, f"sign_up/login_page")

        with allure.step("Sign up with valid username and password"):
            self.login.check_signup_form_title_visibility()
            registered_username = self.data_generator.generate_username()
            self.login.signup(registered_username, self.data_generator.generate_email())
            Helpers.take_screenshot(self.page, f"sign_up_form")

        with allure.step("Fill account information form"):
            self.signup.check_account_info_form_title_visibility()
            birth_date = self.data_generator.generate_date_of_birth()
            self.signup.fill_account_info(self.data_generator.generate_password(), birth_date["day"], birth_date["month"],
                                          birth_date["year"])
            Helpers.take_screenshot(self.page, f"filled_account_info")

        with allure.step("Fill address information form"):
            self.signup.fill_address_info(self.data_generator.generate_firstname(),
                                          self.data_generator.generate_lastname(),
                                          self.data_generator.generate_company_name(),
                                          self.data_generator.generate_address(), self.data_generator.generate_address(),
                                          self.data_generator.generate_state(), self.data_generator.generate_city(),
                                          self.data_generator.generate_zipcode(),
                                          self.data_generator.generate_mobile_number())
            Helpers.take_screenshot(self.page, f"filled_address_info")

        with allure.step("Create account and check success message"):
            self.signup.click_create_account_btn()
            self.account_created.check_msg_title_visibility()
            Helpers.take_screenshot(self.page, f"account_created_success_message")

        with allure.step(f"Navigate to the Home page and verify that 'Logged in as {registered_username}' is visible"):
            self.account_created.click_continue_btn()
            self.navbar.check_logged_in_username_visibility()
            Helpers.take_screenshot(self.page, f"logged_in_user")

        with allure.step("Delete account and check success message"):
            self.navbar.click_delete_account_btn()
            Helpers.take_screenshot(self.page, f"delete_account_page")
            self.delete_account.check_msg_title_visibility()
            Helpers.take_screenshot(self.page, f"account_deleted_success_message")

        with allure.step("Navigate to the Home page"):
            self.delete_account.click_continue_btn()
            Helpers.take_screenshot(self.page, f"home_page")

    def test_registration_with_existing_email(self, test_setup):
        """Test the registration process by attempting to sign up a new user with an existing email.

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        with allure.step("Register the user"):
            registered_username, registered_email, registered_password = Helpers.register_user(test_setup)

        with allure.step("Navigate to the Signup/Login page"):
            self.home.check_home_page_visibility()
            self.navbar.click_signup_login_btn()
            Helpers.take_screenshot(self.page, "sign_up/login_page")

        with allure.step("Sign up with valid username and password"):
            self.login.check_signup_form_title_visibility()
            self.login.signup(self.data_generator.generate_username(), registered_email)
            Helpers.take_screenshot(self.page, "filled_sign_up_form")

        with allure.step("Check signup error message"):
            self.login.check_signup_error_msg_visibility()
            Helpers.take_screenshot(self.page, "sign_up_error_message")
