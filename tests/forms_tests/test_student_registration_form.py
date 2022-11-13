from selene.support.shared import browser
from selene import have, be, command

from tests.test_data.students import dante
from utils.files import generate_absolute_path


def given_opend_registration_form():
    browser.open('/automation-practice-form')


def test_success_submit():
    given_opend_registration_form()

    # WHEN

    browser.element('#firstName').type(dante.first_name)
    browser.element('#lastName').type(dante.last_name)
    browser.element('#userEmail').type(dante.email)
    browser.element(
        f'[id^=gender-radio][value={dante.gender.value}] + .custom-control-label'
    ).click()
    browser.element('#userNumber').type(dante.phone)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(dante.birth_month)
    browser.element('.react-datepicker__year-select').send_keys(dante.birth_year)
    browser.element(
        f'.react-datepicker__month .react-datepicker__day--0{dante.birth_day}:not(.react-datepicker__day--outside-month)'
    ).click()
    for subject in dante.subjects:
        browser.element('#subjectsInput').type(subject.value).press_enter()
    for hobby in dante.hobbies:
        browser.all('[for^=hobbies-checkbox]').by(
            have.exact_text(hobby.value)
        ).first.click()
    browser.element('#uploadPicture').send_keys(generate_absolute_path(dante.picture))
    browser.element('#currentAddress').type(dante.address)
    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click()
    browser.all('#state [id^=react-select-3-option]').by(
        have.exact_text(dante.state)
    ).first.click()
    browser.element('#city').click()
    browser.all('#city [id^=react-select-4-option]').by(
        have.exact_text(dante.city)
    ).first.click()

    # THEN

    browser.element('#submit').perform(command.js.click)
    browser.element('.modal-header #example-modal-sizes-title-lg').should(be.present)
    browser.element('.modal-body').all('td:nth-child(even)').should(
        have.texts(
            f'{dante.first_name} {dante.last_name}',
            dante.email,
            dante.gender.value,
            dante.phone,
            f'{dante.birth_day} {dante.birth_month},{dante.birth_year}',
            ', '.join([subject.value for subject in dante.subjects]),
            ', '.join([hobby.value for hobby in dante.hobbies]),
            dante.picture.split('/')[-1],
            dante.address,
            f'{dante.state} {dante.city}',
        )
    )
