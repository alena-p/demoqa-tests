from selene import command
from selene.support.shared import browser
from selenium.webdriver import Keys


def set_date_by_picking(element, day: str, month: str, year: str):
    browser.element(element).click()
    browser.element('.react-datepicker__month-select').send_keys(month)
    browser.element('.react-datepicker__year-select').send_keys(year)
    browser.element(
        f'.react-datepicker__month .react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
    ).click()


def set_date_by_typing(element, day: str, month: str, year: str):
    browser.element(element).click().send_keys(Keys.HOME).send_keys(
        Keys.SPACE
    ).send_keys(Keys.DELETE * 11)
    browser.element(element).type(f'{day} {month} {year}').press_enter()
