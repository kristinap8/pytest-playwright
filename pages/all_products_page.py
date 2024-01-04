from playwright.sync_api import Page, expect
from pages.base_page import Base
import time

title = '.features_items h2.title'
products_list = '.features_items'
search_product_input = 'input#search_product'
search_btn = 'button#submit_search'
product_names = '.productinfo p'
view_product_btns = 'a[href*="/product_details/"]'

expected_all_products_title = "ALL PRODUCTS"
expected_searched_products_title = "SEARCHED PRODUCTS"


class AllProducts(Base):

    def __init__(self, page: Page):
        super().__init__(page)

    def search_product(self, product_ind) -> str:
        product_name = self.get_text_content_by_ind(product_names, product_ind-1)
        self.type(search_product_input, product_name)
        self.click(search_btn)
        return product_name

    def products_count(self) -> int:
        return self.get_elements_count(product_names)

    def click_first_view_product_btn(self) -> None:
        self.click_by_ind(view_product_btns, 0)

    def check_navigation_to_all_products(self) -> None:
        actual_title = self.get_inner_text(title)
        assert actual_title == expected_all_products_title, \
            f'Expected page to have a "{expected_all_products_title}" title, got "{actual_title}" instead'

    def check_products_list_visibility(self) -> None:
        expect(self.get_element(products_list)).to_be_visible()

    def check_search_results(self, searched_product_name) -> None:
        assert self.is_visible(title), 'Title element is not visible'

        self.pause(500)
        actual_title = self.get_inner_text(title)
        assert actual_title == expected_searched_products_title, \
            f'Expected to page have a "{expected_searched_products_title}" title, got "{actual_title}" instead'

        for i in range(self.get_elements_count(product_names)):
            product_name = self.get_inner_text_by_ind(product_names, i)
            assert searched_product_name in product_name, \
                f'Product name "{product_name}" does not contain the searched text'
            assert self.get_element_by_ind(product_names, i).is_visible(), f'Product "{product_name}" is not visible'
