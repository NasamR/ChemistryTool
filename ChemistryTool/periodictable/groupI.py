from .element import Element


class H(Element):
    __slots__ = ()

    def __repr__(self):
        return 'H'

__all__ = ['H']
