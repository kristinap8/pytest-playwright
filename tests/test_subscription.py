import pytest
import allure

from pages.home_page import Home
from pages.components.footer import Footer
from utils.helpers import Helpers
from utils.data_generator import DataGenerator


@allure.story("Subscription")
class TestSubscription:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home = Home(self.page)
        self.footer = Footer(self.page)
        self.data_generator = DataGenerator()

    def test_subscription(self, test_setup):
        """Verify the subscription functionality on the home page.

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        with allure.step("Check navigation to the Home page"):
            self.home.check_home_page_visibility()

        with allure.step("Scroll to the footer and verify subscription form"):
            self.footer.scroll_to_footer()
            self.footer.check_subscription_title()

        with allure.step("Subscribe with valid email and check success message"):
            self.footer.subscribe(self.data_generator.generate_email())
            self.footer.check_success_msg_visibility()
            Helpers.take_screenshot(self.page, "subscription_success_message")
