from selene.support.shared import browser


def set_date(element, day: str, month: str, year: str):
    browser.element(element).click()
    browser.element('.react-datepicker__month-select').send_keys(month)
    browser.element('.react-datepicker__year-select').send_keys(year)
    browser.element(
        f'.react-datepicker__month .react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
    ).click()
