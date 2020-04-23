from .element import Element


class C(Element):
    __slots__ = ()

    def __repr__(self):
        return 'C'

__all__ = ['C']
