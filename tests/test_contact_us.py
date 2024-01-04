import pytest
import allure

from pages.home_page import Home
from pages.login_page import Login
from pages.delete_account_page import DeleteAccount
from pages.contact_us_page import ContactUs
from pages.components.navbar import Navbar
from utils.data_generator import DataGenerator
from utils.helpers import Helpers


@allure.story('Contact Us Form')
class TestContactUs:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home = Home(self.page)
        self.login = Login(self.page)
        self.delete_account = DeleteAccount(self.page)
        self.contact_us = ContactUs(self.page)
        self.navbar = Navbar(self.page)
        self.data_generator = DataGenerator()

        return self

    def test_contact_us_form_submission(self, test_setup):
        """Verify the proper functionality of the Contact Us form, including successful submission and navigation.

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        with allure.step("Navigate to the Contact Us page"):
            self.home.check_home_page_visibility()
            self.navbar.click_contact_us_btn()
            Helpers.take_screenshot(self.page, "contact_us_page")

        with allure.step("Check the Contact Us form title"):
            self.contact_us.check_form_title()

        with allure.step("Fill the Contact Us form"):
            self.contact_us.fill_contact_us_form(self.data_generator.generate_firstname(),
                                                 self.data_generator.generate_email(),
                                                 self.data_generator.generate_message_subject(),
                                                 self.data_generator.generate_message_text(),
                                                 "data/contact_us_file.txt")
            Helpers.take_screenshot(self.page, "filled_form")

        with allure.step("Submit the form and confirm the dialog"):
            self.contact_us.confirm_the_dialog()
            self.contact_us.click_submit_btn()

        with allure.step("Check the success message"):
            self.contact_us.check_success_msg()
            Helpers.take_screenshot(self.page, "success_message_after_submitting_form")

        with allure.step("Go to the home page"):
            self.contact_us.click_home_btn()
            self.home.check_home_page_visibility()
            Helpers.take_screenshot(self.page, "home_page")
