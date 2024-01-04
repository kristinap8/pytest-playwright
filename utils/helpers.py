import allure


class Helpers:
    @staticmethod
    def register_user(test_setup):
        test_setup.navbar.click_signup_login_btn()

        username = test_setup.data_generator.generate_username()
        email = test_setup.data_generator.generate_email()
        password = test_setup.data_generator.generate_password()

        test_setup.login.signup(username, email)

        birth_date = test_setup.data_generator.generate_date_of_birth()
        test_setup.signup.fill_account_info(
            password,
            birth_date["day"],
            birth_date["month"],
            birth_date["year"]
        )
        test_setup.signup.fill_address_info(
            test_setup.data_generator.generate_firstname(),
            test_setup.data_generator.generate_lastname(),
            test_setup.data_generator.generate_company_name(),
            test_setup.data_generator.generate_address(),
            test_setup.data_generator.generate_address(),
            test_setup.data_generator.generate_state(),
            test_setup.data_generator.generate_city(),
            test_setup.data_generator.generate_zipcode(),
            test_setup.data_generator.generate_mobile_number()
        )
        test_setup.signup.click_create_account_btn()

        test_setup.account_created.click_continue_btn()

        test_setup.navbar.click_logout_btn()
        test_setup.navbar.click_home_btn()

        return username, email, password

    @staticmethod
    def take_screenshot(page, name) -> None:
        allure.attach(
            body=page.screenshot(full_page=True),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
