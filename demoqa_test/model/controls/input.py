from selene.support.shared import browser


def fill_text(element, value):
    browser.element(element).type(value)
