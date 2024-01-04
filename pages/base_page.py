import allure
from playwright.sync_api import Page


class Base:

    def __init__(self, page: Page):
        self.page = page

    def get_element(self, selector):
        return self.page.locator(selector)

    @allure.step("Get element with locator - {selector} and with index - {ind}")
    def get_element_by_ind(self, selector, ind):
        return self.get_element(selector).nth(ind)

    @allure.step('Click locator - {selector}')
    def click(self, selector):
        self.get_element(selector).click()

    @allure.step('Click locator - {selector} with {ind} index')
    def click_by_ind(self, selector, ind):
        self.get_element_by_ind(selector, ind).click()

    @allure.step("Get number of elements with locator - {selector}")
    def get_elements_count(self, selector):
        return self.get_element(selector).count()

    @allure.step("Scroll to locator - {selector}")
    def scroll_to_element(self, selector):
        self.get_element(selector).scroll_into_view_if_needed()

    @allure.step('Type text - {text} into locator - {selector}')
    def type(self, selector, text):
        self.get_element(selector).fill(text)

    @allure.step("Inner text of {selector} locator")
    def get_inner_text(self, selector):
        return self.get_element(selector).inner_text()

    @allure.step("Content text of {selector} locator")
    def get_text_content(self, selector):
        return self.get_element(selector).text_content()

    @allure.step("Content text of {selector} locator with {ind} index")
    def get_text_content_by_ind(self, selector, ind):
        return self.get_element_by_ind(selector, ind).text_content()

    @allure.step("Inner text of {selector} locator with {ind} index")
    def get_inner_text_by_ind(self, selector, ind):
        return self.get_element_by_ind(selector, ind).inner_text()

    @allure.step("Check element with {selector} locator")
    def check_element(self, selector):
        self.get_element(selector).check()

    @allure.step('Select option - {option} in locator - {selector}')
    def select_option_by_value(self, selector, option):
        self.get_element(selector).select_option(option)

    @allure.step('Select option with {option} index in locator - {selector}')
    def select_option_by_index(self, selector, option):
        self.get_element(selector).select_option(index=option)

    def pause(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)

    @allure.step("Accept dialog")
    def accept_dialog(self):
        self.pause(500)
        self.page.once('dialog', lambda dialog: dialog.accept())

    @allure.step("Upload {files} files")
    def upload_files(self, selector, files):
        self.get_element(selector).set_input_files(files)

    @allure.step("Is element - {selector} visible")
    def is_visible(self, selector):
        return self.get_element(selector).is_visible()

    @allure.step("Wait for {url} url")
    def wait_for_url(self, url):
        self.page.wait_for_url(url)
