import allure
import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from demoqa_test.utils import attachments


def pytest_addoption(parser):
    parser.addoption('--browser_version', default='100')


with allure.step('Configure browser'):

    @pytest.fixture(scope="function", autouse=True)
    def browser_config(request):
        browser_version = request.config.getoption('--browser_version')
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {"enableVNC": True, "enableVideo": True},
        }

        options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(
            command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
            options=options,
        )

        browser.config.driver = driver
        browser.config.base_url = "https://demoqa.com"
        browser.config.window_width = 1920
        browser.config.window_height = 900

        yield browser

        attachments.add_html(browser)
        attachments.add_screenshot(browser)
        attachments.add_logs(browser)
        attachments.add_video(browser)
        browser.quit()
