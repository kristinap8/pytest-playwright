import pytest
import allure

from pages.home_page import Home
from pages.all_products_page import AllProducts
from pages.product_details_page import ProductDetails
from pages.components.navbar import Navbar
from utils.helpers import Helpers
from utils.data_generator import DataGenerator


@allure.story("Products")
class TestProducts:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home = Home(self.page)
        self.all_products = AllProducts(self.page)
        self.product_details = ProductDetails(self.page)
        self.navbar = Navbar(self.page)
        self.data_generator = DataGenerator()

    def test_all_products_and_product_detail(self, test_setup) -> None:
        """Test the navigation to ALL PRODUCTS and the visibility of product details.

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        with allure.step("Navigate to the Products page"):
            self.home.check_home_page_visibility()
            self.navbar.click_products_btn()
            Helpers.take_screenshot(self.page, "products_page")

        with allure.step("Check navigation to Products page and products list visibility"):
            self.all_products.check_navigation_to_all_products()
            self.all_products.check_products_list_visibility()

        with allure.step("Click the first 'View Product' button"):
            self.all_products.click_first_view_product_btn()
            Helpers.take_screenshot(self.page, "product_details_page")

        with allure.step("Check first product details navigation and visibility"):
            self.product_details.check_first_product_details_navigation()
            self.product_details.check_product_details_visibility()

    def test_search_product(self, test_setup):
        """Test searching for a product on the ALL PRODUCTS page.

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        with allure.step("Navigate to the Products page"):
            self.home.check_home_page_visibility()
            self.navbar.click_products_btn()
            Helpers.take_screenshot(self.page, "products_page")

        with allure.step("Check navigation to Products page and products list visibility"):
            self.all_products.check_navigation_to_all_products()

        with allure.step("Search for a product and check search results"):
            product_ind = self.data_generator.generate_random_number(high=self.all_products.products_count())
            searched_product_name = self.all_products.search_product(product_ind)
            Helpers.take_screenshot(self.page, f"search_entered_{searched_product_name}")
            self.all_products.check_search_results(searched_product_name)
            Helpers.take_screenshot(self.page, f"search_results_{searched_product_name}")
