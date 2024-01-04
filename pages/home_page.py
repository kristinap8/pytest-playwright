from playwright.sync_api import Page, expect
from pages.base_page import Base

slider = 'section[id=slider]'


class Home(Base):
    def __init__(self, page: Page):
        super().__init__(page)

    def check_home_page_visibility(self):
        expect(self.get_element(slider)).to_be_visible()
