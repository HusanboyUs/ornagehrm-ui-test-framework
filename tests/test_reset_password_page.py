from playwright.sync_api import Page, expect
import pytest
import time

# pages
from pages import LoginPage, PasswordResetPage


@pytest.mark.usefixtures("loginPage")
class TestResetPasswordPage:
    """
    Tests to verify test password login page
    """

    @pytest.mark.password_reset
    def test_open_password_reset_page(self, loginPage):
        password_reset_page = loginPage.click_password_reset_page()
        expect(password_reset_page.password_reset_form).to_be_visible()

    @pytest.mark.password_reset
    def test_send_username_to_password_reset_with_empty_username(self, loginPage):
        password_reset_page = loginPage.click_password_reset_page()
        password_reset_page.enter_username_to_form("")
    
    @pytest.mark.password_reset
    def test_send_username_to_password_reset(self, loginPage):
        password_reset_page = loginPage.click_password_reset_page()
        password_reset_page.enter_username_to_form("Admin")
        expect(password_reset_page.password_reset_link_sent_form).to_be_visible()
        



    