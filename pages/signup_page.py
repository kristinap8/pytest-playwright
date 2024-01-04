from playwright.sync_api import Page, expect
from pages.base_page import Base
from utils.data_generator import DataGenerator

account_info_form_title = '//*[text()="Enter Account Information"]'
password_input = 'input[id="password"]'
day_of_birth_dropdown = 'select[id="days"]'
month_of_birth_dropdown = 'select[id="months"]'
year_of_birth_dropdown = 'select[id="years"]'
newsletter_checkbox = 'input[id="newsletter"]'
offers_checkbox = 'input[id="optin"]'
first_name_input = 'input[id="first_name"]'
last_name_input = 'input[id="last_name"]'
company_input = 'input[id="company"]'
address1_input = 'input[id="address1"]'
address2_input = 'input[id="address2"]'
country_dropdown = 'select[id="country"]'
state_input = 'input[id="state"]'
city_input = 'input[id="city"]'
zipcode_input = 'input[id="zipcode"]'
mobile_number_input = 'input[id="mobile_number"]'
create_account_btn = 'button[data-qa="create-account"]'
gender_titles = ['input[id="id_gender1"]', 'input[id="id_gender2"]']


class Signup(Base):
    def __init__(self, page: Page):
        super().__init__(page)

        self.data_generator = DataGenerator()

    def select_title(self) -> None:
        random_ind = self.data_generator.generate_random_number(len(gender_titles) - 1, 0)
        self.check_element(gender_titles[random_ind])

    def select_day_of_birth(self, day_of_birth) -> None:
        self.select_option_by_value(day_of_birth_dropdown, day_of_birth)

    def select_month_of_birth(self, month_of_birth) -> None:
        self.select_option_by_value(month_of_birth_dropdown, month_of_birth)

    def select_year_of_birth(self, year_of_birth) -> None:
        self.select_option_by_value(year_of_birth_dropdown, year_of_birth)

    def select_country(self) -> None:
        self.select_option_by_index(country_dropdown, self.data_generator.generate_random_number(1, 7))

    def fill_account_info(self, password, day_of_birth, month_of_birth, year_of_birth,
                          sign_up_for_newsletter=True, receive_special_offers=True) -> None:
        self.select_title()
        self.type(password_input, password)
        self.select_day_of_birth(day_of_birth)
        self.select_month_of_birth(month_of_birth)
        self.select_year_of_birth(year_of_birth)
        if sign_up_for_newsletter:
            self.check_element(newsletter_checkbox)
        if receive_special_offers:
            self.check_element(offers_checkbox)

    def fill_address_info(self, firstname, lastname, company, address1, address2, state, city,
                          zipcode, mobile_number) -> None:
        self.type(first_name_input, firstname)
        self.type(last_name_input, lastname)
        self.type(company_input, company)
        self.type(address1_input, address1)
        self.type(address2_input, address2)
        self.type(state_input, state)
        self.type(city_input, city)
        self.type(zipcode_input, zipcode)
        self.type(mobile_number_input, mobile_number)

    def click_create_account_btn(self) -> None:
        self.click(create_account_btn)

    def check_account_info_form_title_visibility(self) -> None:
        self.pause(500)
        expect(self.get_element(account_info_form_title)).to_be_visible()
