from typing import Optional


class Element:
    def __init__(self, isotope: Optional[int] = None):
        self.isotope = isotope


__all__ = ['Element']
