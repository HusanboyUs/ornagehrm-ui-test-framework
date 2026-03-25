from playwright.sync_api import Page, expect
import pytest

# pages
from pages import LoginPage


@pytest.mark.usefixtures("loginPage")
class TestLoginPage:
    """
    Tests to verify login scenario functionality under different test cases
    """

    @pytest.mark.parametrize("username, password", [
        ("some__!", "passWord_!3#"),
        ("randomuser", "p___"),
        ("123", "!3#"),
    ])
    def test_login_with_incorrect_credentials(self, loginPage, username, password):
        # act
        loginPage.login(
            username=username,
            password=password
        )
        # expect
        expect(loginPage)

    def test_login_with_correct_credentials(self, login):
        print("I am test case2")