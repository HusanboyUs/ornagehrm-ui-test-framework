import pytest
from playwright.sync_api import sync_playwright


from pages import LoginPage

@pytest.fixture(scope="session", autouse=True)
def browser():
    with sync_playwright() as plyw:
        browser = plyw.webkit.launch(
            headless=False
        )
        yield browser
        browser.close()


@pytest.fixture(scope="class", autouse=True)
def contextPage(browser):
    page = browser.new_page()
    yield page
    page.close()


# -------------------------------------- PAGES ---------------------------------------------------
@pytest.fixture(scope="class", autouse=False)
def loginPage(contextPage) -> LoginPage:
    return LoginPage(page=contextPage)

@pytest.fixture(scope="class", autouse=False)
def login():
    pass 


# not sure about this one!
@pytest.fixture(scope="class", autouse=False)
def logout():
    pass