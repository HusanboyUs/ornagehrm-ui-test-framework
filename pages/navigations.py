from .basePage import BasePage



class Navigation(BasePage):

    def __init__(self, page):
        super().__init__(page=page)

    def navigate_to(self):
        self.page.locator().click()
        