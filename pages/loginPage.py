from .basePage import BasePage
from .passwordResetPage import PasswordResetPage



class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page=page)

    @property
    def username_input(self):
        return self.page.get_by_placeholder("Username")
    
    @property
    def password_input(self):
        return self.page.get_by_placeholder("Password")
    
    @property
    def login_error_alert(self):
        return self.page.locator("//div[@role='alert']//p")

    def login(self, username, password):
        self.username_input.fill(value=username, force=True)
        self.password_input.fill(value=password, force=True)
        self.page.get_by_role(role="button", name="Login").click()

    def click_password_reset_page(self):
        self.page.locator("xpath=//*[@class='orangehrm-login-forgot']").click()
        return PasswordResetPage(page=self.page)