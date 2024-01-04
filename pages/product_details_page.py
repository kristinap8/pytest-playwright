from playwright.sync_api import Page, expect
from pages.base_page import Base
import re

product_name = '.product-information h2'
product_category = '//*[@class="product-information"]//*[contains(text(), "Category")]'
product_price = '//*[@class="product-information"]//*[contains(text(), "Rs.")]'
product_availability = '//*[@class="product-information"]//*[contains(text(), "Availability")]'
product_condition = '//*[@class="product-information"]//*[contains(text(), "Condition")]'
product_brand = '//*[@class="product-information"]//*[contains(text(), "Brand")]'

expected_url_to_first_product = '/product_details/1'


class ProductDetails(Base):

    def __init__(self, page: Page):
        super().__init__(page)

    def check_first_product_details_navigation(self) -> None:
        expect(self.page).to_have_url(re.compile(expected_url_to_first_product + '$'))

    def check_product_details_visibility(self) -> None:
        expect(self.get_element(product_name)).to_be_visible()
        expect(self.get_element(product_category)).to_be_visible()
        expect(self.get_element(product_price)).to_be_visible()
        expect(self.get_element(product_availability)).to_be_visible()
        expect(self.get_element(product_condition)).to_be_visible()
        expect(self.get_element(product_brand)).to_be_visible()
