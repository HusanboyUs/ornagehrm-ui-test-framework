from playwright.sync_api import Page, expect
import pytest


# pages
from pages import LoginPage


@pytest.mark.usefixtures("loginPage")
class TestLoginPage:
    """
    Tests to verify login scenario functionality under different test cases
    """

    @pytest.mark.parametrize("username, password, error_message", [
        ("some__!", "passWord_!3#", "Invalid credentials"),
        ("randomuser", "p___", "Invalid credentials"),
        ("123", "!3#", "Invalid credentials"),
    ])
    def test_login_with_incorrect_credentials(self, loginPage, username, password, error_message):
        # act
        loginPage.login(
            username=username,
            password=password
        )
        # assert
        expect(loginPage.login_error_alert).to_have_text(error_message)

    def test_login_with_correct_credentials(self, loginPage):
        loginPage.login(
            username="Admin",
            password="admin123"
        )
        # assert
        expect(loginPage.login_error_alert).not_to_be_visible()
        expect(loginPage.username_input).not_to_be_visible()
        expect(loginPage.password_input).not_to_be_visible()
