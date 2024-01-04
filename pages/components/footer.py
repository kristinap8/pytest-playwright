from playwright.sync_api import Page, expect
from pages.base_page import Base

footer = 'footer[id="footer"]'
subscription_title = '#footer h2'
email_input = '#susbscribe_email'
subscribe_btn = '#subscribe'
success_msg = '//*[text()="You have been successfully subscribed!"]'

expected_title = "SUBSCRIPTION"


class Footer(Base):

    def __init__(self, page: Page):
        super().__init__(page)

    def scroll_to_footer(self) -> None:
        self.scroll_to_element(footer)

    def subscribe(self, email) -> None:
        self.type(email_input, email)
        self.click(subscribe_btn)

    def check_subscription_title(self) -> None:
        actual_title = self.get_inner_text(subscription_title)
        assert actual_title == expected_title, \
            f'Expected the subscription title to be "{expected_title}", but got "{actual_title}" instead'

    def check_success_msg_visibility(self) -> None:
        expect(self.get_element(success_msg)).to_be_visible()
