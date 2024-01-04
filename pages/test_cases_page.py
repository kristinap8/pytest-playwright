from playwright.sync_api import Page
from pages.base_page import Base

title = '.container h2.title'
expected_title = "Test Cases"


class TestCases(Base):
    __test__ = False

    def __init__(self, page: Page):
        super().__init__(page)

    def check_navigation_to_test_cases(self) -> None:
        actual_title = self.get_text_content(title)
        assert actual_title == expected_title, \
            f'Expected page to have the "{expected_title}" title, got "{actual_title}" instead'
