from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name_input = page.locator("#AccountFrm_firstname")
        self.last_name_input = page.locator("#AccountFrm_lastname")
        self.email_input = page.locator("#AccountFrm_email")
        self.address_input = page.locator("#AccountFrm_address_1")
        self.city_input = page.locator("#AccountFrm_city")
        self.region_select = page.locator("#AccountFrm_zone_id")
        self.postcode_input = page.locator("#AccountFrm_postcode")
        self.login_name_input = page.locator("#AccountFrm_loginname")
        self.password_input = page.locator("#AccountFrm_password")
        self.confirm_password_input = page.locator("#AccountFrm_confirm")
        self.agree_checkbox = page.locator("#AccountFrm_agree")
        self.continue_button = page.get_by_role("button", name="Continue")

    def fill_registration_form(self, user_data: dict):
        self.first_name_input.fill(user_data["first_name"])
        self.last_name_input.fill(user_data["last_name"])
        self.email_input.fill(user_data["email"])
        self.address_input.fill(user_data["address"])
        self.city_input.fill(user_data["city"])
        self.region_select.select_option(label=user_data["region"])
        self.postcode_input.fill(user_data["postcode"])
        self.login_name_input.fill(user_data["login_name"])
        self.password_input.fill(user_data["password"])
        self.confirm_password_input.fill(user_data["password"])
        self.agree_checkbox.check()
        self.continue_button.click()