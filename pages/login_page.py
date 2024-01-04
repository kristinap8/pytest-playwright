from playwright.sync_api import Page, expect
from pages.base_page import Base

signup_form_title = '//*[text()="New User Signup!"]'
signup_name_input = 'input[data-qa="signup-name"]'
signup_email_input = 'input[data-qa="signup-email"]'
signup_btn = 'button[data-qa = "signup-button"]'
signup_error_msg = '//*[text()="Email Address already exist!"]'
login_error_msg = '//*[text()="Your email or password is incorrect!"]'
login_form_title = '//*[text()="Login to your account"]'
login_email_input = 'input[data-qa="login-email"]'
login_password_input = 'input[data-qa="login-password"]'
login_btn = 'button[data-qa = "login-button"]'


class Login(Base):

    def __init__(self, page: Page):
        super().__init__(page)

    def signup(self, name, email) -> None:
        self.type(signup_name_input, name)
        self.type(signup_email_input, email)
        self.click(signup_btn)

    def login(self, email, password) -> None:
        self.type(login_email_input, email)
        self.type(login_password_input, password)
        self.click(login_btn)

    def check_signup_form_title_visibility(self) -> None:
        expect(self.get_element(signup_form_title)).to_be_visible()

    def check_signup_error_msg_visibility(self) -> None:
        expect(self.get_element(signup_error_msg)).to_be_visible()

    def check_login_form_title_visibility(self) -> None:
        expect(self.get_element(login_form_title)).to_be_visible()

    def check_login_error_msg_visibility(self) -> None:
        expect(self.get_element(login_error_msg)).to_be_visible()
