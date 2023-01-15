from typing import Tuple
import selene


class Tags:
    def __init__(self, element: selene.Element):
        self.element = element

    def add_by_autocomplete(self, data: Tuple):
        for item in data:
            self.element.type(item.value).press_enter()
