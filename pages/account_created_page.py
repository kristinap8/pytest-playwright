from playwright.sync_api import Page, expect
from pages.base_page import Base

msg_title = '*[data-qa="account-created"]'
continue_btn = 'a[data-qa="continue-button"]'


class AccountCreated(Base):

    def __init__(self, page: Page):
        super().__init__(page)

    def click_continue_btn(self) -> None:
        self.click(continue_btn)

    def check_msg_title_visibility(self) -> None:
        expect(self.get_element(msg_title)).to_be_visible()
