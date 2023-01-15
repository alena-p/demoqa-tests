from typing import Tuple

import selene


class Checkbox:
    def __init__(self, elements: selene.Collection):
        self.elements = elements

    def set(self, data: Tuple):
        for item in data:
            self.elements.by(selene.have.exact_text(item.value)).first.click()
