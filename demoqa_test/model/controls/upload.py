from selene.support.shared import browser
from demoqa_test.utils.files import generate_absolute_path


def file(element, file_path: str):
    browser.element(element).send_keys(generate_absolute_path(file_path))
