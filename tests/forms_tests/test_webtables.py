from selene.support.shared import browser
from selene import have, be


def given_opened_webtables():
    browser.open("/webtables")


def test_add_raw():
    given_opened_webtables()

    initial_raws_quantity = browser.all(".action-buttons").size()

    browser.element("#addNewRecordButton").click()
    browser.element("#firstName").type("Lester")
    browser.element("#lastName").type("Nicole")
    browser.element("#userEmail").type("zadojituk@mailinator.com")
    browser.element("#age").type("50")
    browser.element("#salary").type("100000")
    browser.element("#department").type("Accountant")
    browser.element("#submit").click()
    browser.all(".action-buttons").should(have.size(initial_raws_quantity + 1))
    browser.all(".rt-tr-group")[initial_raws_quantity].all(".rt-td").should(
        have.texts(
            'Lester',
            'Nicole',
            '50',
            'zadojituk@mailinator.com',
            '100000',
            'Accountant',
            '',
        )
    )


def test_delete_raw(raw_number=2):
    given_opened_webtables()

    initial_raws_quantity = browser.all(".action-buttons").size()
    raw_after_deleted = browser.all(".rt-tr-group")[raw_number].all(".rt-td")
    browser.all("#delete-record-1")[raw_number - 1]
    browser.all(".action-buttons").should(have.size(initial_raws_quantity - 1))
