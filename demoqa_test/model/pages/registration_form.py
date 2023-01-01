from typing import Tuple

from selene import have, be, command
from selene.support.shared import browser

from demoqa_test.model.controls.upload import Upload
from demoqa_test.model.controls.datepicker import DatePicker
from demoqa_test.model.controls.dropdown import Dropdown
from demoqa_test.model.controls.input import Input
from demoqa_test.model.external import google
from demoqa_test.model.test_data.students import Subject, Hobby, Gender, Student


def set_gender(value: Gender):
    browser.element(
        f'[id^=gender-radio][value={value}] + .custom-control-label'
    ).click()


def set_subjects(subjects: Tuple[Subject]):
    for subject in subjects:
        browser.element('#subjectsInput').type(subject.value).press_enter()


def set_hobbies(hobbies: Tuple[Hobby]):
    for hobby in hobbies:
        browser.all('[for^=hobbies-checkbox]').by(
            have.exact_text(hobby.value)
        ).first.click()


def given_opened():
    browser.open('/automation-practice-form')
    google.remove_ads(amount=3, timeout=6)
    google.remove_ads(amount=1, timeout=2)


class RegistrationForm:
    def __init__(self):
        self.first_name = Input(browser.element('#firstName'))
        self.last_name = Input(browser.element('#lastName'))
        self.email = Input(browser.element('#userEmail'))
        self.phone = Input(browser.element('#userNumber'))
        self.address = Input(browser.element('#currentAddress'))
        self.state = Dropdown(browser.element('#state'))
        self.city = Dropdown(browser.element('#city'))
        self.birthday = DatePicker(browser.element('#dateOfBirthInput'))
        self.upload = Upload(browser.element('#uploadPicture'))

    def fill_data(self, student: Student):
        given_opened()

        self.first_name.fill_text(student.first_name)
        self.last_name.fill_text(student.last_name)
        self.email.fill_text(student.email)
        set_gender(student.gender.value)
        self.phone.fill_text(student.phone)
        self.birthday.set_date_by_picking(
            student.birth_day,
            student.birth_month,
            student.birth_year,
        )
        set_subjects(student.subjects)
        set_hobbies(student.hobbies)
        self.upload.file(student.picture)
        self.address.fill_text(student.address)
        self.state.element.perform(command.js.scroll_into_view)
        self.state.select_by_option(student.state)
        self.city.select_by_option(student.city)
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)
        return self

    def should_have_registered(self, student: Student):
        browser.element('.modal-header #example-modal-sizes-title-lg').should(
            be.present
        )

        browser.element('.modal-body').all('td:nth-child(even)').should(
            have.texts(
                [
                    f'{student.first_name} {student.last_name}',
                    student.email,
                    student.gender.value,
                    student.phone,
                    f'{student.birth_day} {student.birth_month},{student.birth_year}',
                    ', '.join([subject.value for subject in student.subjects]),
                    ', '.join([hobby.value for hobby in student.hobbies]),
                    student.picture.split('/')[-1],
                    student.address,
                    f'{student.state} {student.city}',
                ]
            )
        )
        return self
