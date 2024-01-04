import pytest
import allure

from playwright.sync_api import Playwright

disable_loggers = []
blocked_resources_names = ["googleads", "fonts.googleapis.com",
                           "pagead2.googlesyndication.com", 'tpc.googlesyndication.com']


@pytest.fixture(scope='function')
def new_page(playwright: Playwright, request):
    browser_name = request.config.getoption('--browser_name')
    headless = False if request.config.getoption("--headed") else True
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=headless)
    if browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    if browser_name == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.route(
        "**/*",
        lambda route: route.abort()
        if any(resource_name in route.request.url for resource_name in blocked_resources_names)
        else route.continue_()
    )
    page.goto(f'https://automationexercise.com/', wait_until="load", timeout=60000)
    yield page
    browser.close()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chromium')


def pytest_runtest_makereport(item, call) -> None:
    if call.when == "call":
        if call.excinfo is not None and "new_page" in item.funcargs:
            page = item.funcargs["new_page"]

            allure.attach(
                page.screenshot(full_page=True, type='png'),
                name=f"{item.nodeid}.png",
                attachment_type=allure.attachment_type.PNG
            )
