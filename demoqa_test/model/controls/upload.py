import selene
from demoqa_test.utils.files import generate_absolute_path


class Upload:
    def __init__(self, element: selene.Element):
        self.element = element

    def file(self, file_path: str):
        self.element.send_keys(generate_absolute_path(file_path))
