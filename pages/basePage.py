from playwright.sync_api import Page



class BasePage:

    def __init__(self, page:Page):
        self.page:Page = page

    def refresh_page(self):
        self.page.reload()
    
    @property
    def get_page_titlt(self):
        return self.page.title()
    
    def wait_for_page_status(self):
        self.page.wait_for_load_state('load')
        self.page.wait_for_load_state('domcontentloaded')