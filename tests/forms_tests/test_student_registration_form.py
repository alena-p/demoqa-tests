import allure
from allure_commons.types import Severity

from demoqa_test.model.test_data.students import dante

from demoqa_test.model import app


@allure.tag("ui test")
@allure.severity(Severity.CRITICAL)
@allure.story("Registration form")
@allure.feature("Forms")
@allure.label("owner", "Potegova")
@allure.description("Verify registration process is successful")
def test_success_submit():

    with allure.step('Open registration form'):
        app.registration_form.given_opened()

    # WHEN

    with allure.step('Enter student\'s registration data'):
        app.registration_form.enter_first_name(dante.first_name)
        app.registration_form.enter_last_name(dante.last_name)
        app.registration_form.enter_email(dante.email)
        app.registration_form.set_gender(dante.gender.value)
        app.registration_form.enter_phone(dante.phone)
        app.registration_form.set_birthday(
            dante.birth_day, dante.birth_month, dante.birth_year
        )
        app.registration_form.set_subjects(dante.subjects)
        app.registration_form.set_hobbies(dante.hobbies)
        app.registration_form.upload_student_photo(dante.picture)
        app.registration_form.enter_address(dante.address)
        app.registration_form.scroll_to_bottom()
        app.registration_form.set_state(dante.state)
        app.registration_form.set_city(dante.city)

    # THEN

    with allure.step('Send form'):
        app.registration_form.submit()

    with allure.step('Verify all sent data correctly submitted'):
        app.registration_form.check_header()
        app.registration_form.check_data(
            [
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
            ]
        )
