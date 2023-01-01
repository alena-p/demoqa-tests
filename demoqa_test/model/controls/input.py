import selene


class Input:
    def __init__(self, element: selene.Element):
        self.element = element

    def fill_text(self, value):
        self.element.type(value)
