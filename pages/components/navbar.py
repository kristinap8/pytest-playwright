from playwright.sync_api import Page, expect
from pages.base_page import Base

home_btn = '.nav a[href="/"]'
signup_login_btn = '.nav a[href="/login"]'
logged_in_username = '.nav .fa-user'
delete_account_btn = '.nav a[href="/delete_account"]'
logout_btn = '.nav a[href="/logout"]'
contact_us_btn = '.nav a[href="/contact_us"]'
products_btn = '.nav a[href="/products"]'
test_cases_btn = '.nav a[href="/test_cases"]'
dismiss_add_btn = '#ad_iframe'

login_url = '*/login'
delete_account_url = '*/delete_account'
contact_us_url = '*/contact_us'
all_products_url = '*/products'
test_cases_url = '*/test_cases'


class Navbar(Base):

    def __init__(self, page: Page):
        super().__init__(page)

    def click_home_btn(self) -> None:
        self.click(home_btn)

    def click_signup_login_btn(self) -> None:
        self.click(signup_login_btn)
        self.wait_for_url(login_url)

    def click_delete_account_btn(self) -> None:
        self.click(delete_account_btn)
        self.wait_for_url(delete_account_url)

    def click_logout_btn(self) -> None:
        self.click(logout_btn)

    def click_contact_us_btn(self) -> None:
        self.click(contact_us_btn)
        self.wait_for_url(contact_us_url)

    def click_products_btn(self) -> None:
        self.click(products_btn)
        self.wait_for_url(all_products_url)

    def click_test_cases_btn(self) -> None:
        self.click(test_cases_btn)
        self.wait_for_url(test_cases_url)

    def check_logged_in_username_visibility(self) -> None:
        expect(self.get_element(logged_in_username)).to_be_visible()
