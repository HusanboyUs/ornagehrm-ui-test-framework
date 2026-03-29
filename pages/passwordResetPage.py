from .basePage import BasePage



class PasswordResetPage(BasePage):

    def __init__(self,page):
        super().__init__(page=page)

    @property
    def password_reset_form(self):
        return self.page.locator("xpath=//form[@class='oxd-form']")
    
    @property
    def password_reset_link_sent_form(self):
        return self.page.locator("xpath=//h6[contains(@class, 'forgot-password-title')]")
    
    def enter_username_to_form(self, username):
        self.wait_for_page_status()
        self.page.locator("xpath=//input[@placeholder='Username']").fill(username)
        self.page.locator("xpath=//*[contains(@class,'button--reset')]").click()