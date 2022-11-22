from typing import Tuple, List

from selene import have, be, command
from selene.support.shared import browser

from demoqa_test.model import controls
from demoqa_test.model.test_data import Subject, Hobby, Gender

state = browser.element('#state')


def given_opened():
    browser.open('/automation-practice-form')


def enter_first_name(value: str):
    controls.input.fill_text('#firstName', value)


def enter_last_name(value: str):
    controls.input.fill_text('#lastName', value)


def enter_email(value: str):
    controls.input.fill_text('#userEmail', value)


def enter_phone(value: str):
    controls.input.fill_text('#userNumber', value)


def enter_address(value: str):
    controls.input.fill_text('#currentAddress', value)


def set_gender(value: Gender):
    browser.element(
        f'[id^=gender-radio][value={value}] + .custom-control-label'
    ).click()


def set_birthday(birth_day: str, birth_month: str, birth_year: str):
    controls.datepicker.set_date_by_typing(
        '#dateOfBirthInput', birth_day, birth_month, birth_year
    )

    # controls.datepicker.set_date_by_picking(
    #     '#dateOfBirthInput', birth_day, birth_month, birth_year
    # )


def upload_student_photo(value):
    controls.upload.file('#uploadPicture', value)


def set_subjects(subjects: Tuple[Subject]):
    for subject in subjects:
        browser.element('#subjectsInput').type(subject.value).press_enter()


def set_hobbies(hobbies: Tuple[Hobby]):
    for hobby in hobbies:
        browser.all('[for^=hobbies-checkbox]').by(
            have.exact_text(hobby.value)
        ).first.click()


def set_state(value: str):
    controls.dropdown.select_by_option(state, value)


def set_city(value: str):
    controls.dropdown.select_by_option(browser.element('#city'), value)


def scroll_to_bottom():
    state.perform(command.js.scroll_into_view)


def submit():
    browser.element('#submit').perform(command.js.click)


def check_header():
    browser.element('.modal-header #example-modal-sizes-title-lg').should(be.present)


def check_data(data: List):
    browser.element('.modal-body').all('td:nth-child(even)').should(have.texts(data))
