from faker import Faker


class DataGenerator:
    def __init__(self):
        self.fake = Faker(locale="en_US")

    def generate_random_number(self, high, low=1) -> int:
        return self.fake.random_int(low, high)

    def generate_username(self) -> str:
        return self.fake.user_name()

    def generate_email(self) -> str:
        return self.fake.email()

    def generate_password(self) -> str:
        return self.fake.password()

    def generate_date_of_birth(self) -> dict:
        birth_date = self.fake.date_of_birth(minimum_age=18, maximum_age=65)
        return {"day": str(birth_date.day), "month": birth_date.strftime("%B"), "year": str(birth_date.year)}

    def generate_firstname(self) -> str:
        return self.fake.first_name()

    def generate_lastname(self) -> str:
        return self.fake.last_name()

    def generate_company_name(self) -> str:
        return self.fake.company()

    def generate_address(self) -> str:
        return self.fake.address()

    def generate_state(self) -> str:
        return self.fake.state()

    def generate_city(self) -> str:
        return self.fake.city()

    def generate_zipcode(self) -> str:
        return self.fake.zipcode()

    def generate_mobile_number(self) -> str:
        return self.fake.phone_number()

    def generate_message_subject(self) -> str:
        return self.fake.sentence()

    def generate_message_text(self) -> str:
        return self.fake.text()

