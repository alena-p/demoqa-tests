from selene import have
from selene.support.shared import browser


def select_by_option(element, value):
    element.click()
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(value)
    ).first.click()
