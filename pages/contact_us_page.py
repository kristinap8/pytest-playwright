from playwright.sync_api import Page, expect
from pages.base_page import Base

form_title = '.contact-form .title'
name_input = 'input[data-qa="name"]'
email_input = 'input[data-qa="email"]'
subject_input = 'input[data-qa="subject"]'
message_textarea = 'textarea[id="message"]'
file_input = 'input[name="upload_file"]'
submit_btn = 'input[data-qa="submit-button"]'
success_msg = '.status.alert.alert-success'
home_btn = '.btn-success'

expected_title = "GET IN TOUCH"
expected_success_msg = "Success! Your details have been submitted successfully."


class ContactUs(Base):

    def __init__(self, page: Page):
        super().__init__(page)

    def fill_contact_us_form(self, name, email, subject, message, file_path) -> None:
        self.type(name_input, name)
        self.type(email_input, email)
        self.type(subject_input, subject)
        self.type(message_textarea, message)
        self.upload_files(file_input, file_path)

    def confirm_the_dialog(self) -> None:
        self.accept_dialog()

    def click_submit_btn(self) -> None:
        self.click(submit_btn)

    def click_home_btn(self) -> None:
        self.click(home_btn)

    def check_form_title(self):
        actual_title = self.get_inner_text(form_title)
        assert actual_title == expected_title, \
            f'Contact us form title expected to be "{expected_title}", got "{actual_title}" instead'
        expect(self.get_element(form_title)).to_be_visible()

    def check_success_msg(self) -> None:
        actual_success_msg = self.get_inner_text(success_msg)
        assert actual_success_msg == expected_success_msg, \
            f'After submitting the "Contact Us" form, expected to see {expected_success_msg},\
             got "{actual_success_msg}" instead.'
        expect(self.get_element(success_msg)).to_be_visible()






