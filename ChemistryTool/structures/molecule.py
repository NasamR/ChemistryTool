from .abc import MoleculeABC
from ..algorithms import Isomorphism
from ..periodictable.element import Element


class Molecule(Isomorphism, MoleculeABC):
    def add_atom(self, element: str, number: int):
        if isinstance(element, str) and isinstance(number, int):
            if number in self._atoms:
                raise KeyError('This atom already exists')
            else:
                self._atoms[number] = element
                self._bonds[number] = {}
        else:
            raise TypeError('Atom should be string and number should be integer')

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if start_atom in self._atoms and end_atom in self._atoms:
            if start_atom == end_atom:
                raise KeyError('Atoms should be different')
            elif self._bonds[start_atom].get(end_atom, False):
                raise KeyError('This bond already exists')
            else:
                self._bonds[start_atom].update({end_atom: bond_type})
                self._bonds[end_atom].update({start_atom: bond_type})
        else:
            raise KeyError('This atoms do not exist')

    def get_atom(self, number: int) -> Element:
        return self._atoms[number]

    def get_bond(self, start_atom: int, end_atom: int) -> int:
        return self._bonds[start_atom][end_atom]

    def delete_atom(self, number: int):
        for i in self._bonds[number]:
            del self._bonds[i][number]
        del self._bonds[number]
        del self._atoms[number]

    def delete_bond(self, start_atom: int, end_atom: int):
        del self._bonds[start_atom][end_atom]
        del self._bonds[end_atom][start_atom]

    def update_atom(self, element: Element, number: int):
        if isinstance(element, Element):
            self._atoms[number] = element
        else:
            raise TypeError('')

    def update_bond(self, start_atom: int, end_atom: int, bond_type: int):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __str__(self):
        pass


__all__ = ['Molecule']
