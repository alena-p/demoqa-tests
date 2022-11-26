import allure
import pytest
from selene.support.shared import browser

with allure.step('Configure browser'):

    @pytest.fixture(scope="function", autouse=True)
    def browser_config():
        browser.config.base_url = "https://demoqa.com"
        browser.config.browser_name = "chrome"

        yield
