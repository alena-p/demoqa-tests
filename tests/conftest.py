import allure
import pytest
from selene.support.shared import browser

from demoqa_test.utils import attachments

with allure.step('Configure browser'):

    @pytest.fixture(scope="function", autouse=True)
    def browser_config():
        browser.config.base_url = "https://demoqa.com"
        browser.config.browser_name = "chrome"

        yield browser

        attachments.add_html(browser)
        attachments.add_screenshot(browser)
        attachments.add_logs(browser)
        attachments.add_video(browser)
        browser.quit()
