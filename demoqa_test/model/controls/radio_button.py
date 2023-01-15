import selene


class RadioButton:
    def __init__(self, element: selene.Element):
        self.element = element

    def set(self):
        self.element.click()
