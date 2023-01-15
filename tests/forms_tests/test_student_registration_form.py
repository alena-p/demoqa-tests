import allure
from allure_commons.types import Severity
from demoqa_test.model.test_data.students import Student, Gender
from demoqa_test.model import app


@allure.tag("ui test")
@allure.severity(Severity.CRITICAL)
@allure.story("Registration form")
@allure.feature("Forms")
@allure.label("owner", "Potegova")
@allure.description("Verify registration process is successful")
def test_success_submit():

    # GIVEN
    with allure.step('Application is ready'):
        app.registration_form.given_opened()

    with allure.step('Define student'):
        dante = Student(first_name='Dante', last_name='Hardy', gender=Gender.Male)

    # WHEN
    with allure.step('Enter student\'s registration data and send form'):
        app.registration_form.fill_data(dante).submit()

    # THEN
    with allure.step('Verify all sent data correctly submitted'):
        app.registration_form.should_have_registered(dante)
