from .abc import MoleculeABC
from ..algorithms import Isomorphism


class Molecule(Isomorphism, MoleculeABC):
    def add_atom(self, element: str, number: int):
        if isinstance(element, str) and isinstance(number, int):
            if number in self._atoms:
                raise KeyError('This atom already exists')
            else:
                self._atoms[number] = element
        else:
            raise TypeError('Atom should be string and number should be integer')

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if isinstance(start_atom, int) and isinstance(end_atom, int) and isinstance(bond_type, int):
            if start_atom in self._atoms and end_atom in self._atoms:
                if start_atom == end_atom:
                    raise KeyError('Atoms should be different')
                elif start_atom in self._bonds:
                    self._bonds[start_atom].update({end_atom: bond_type})
                    if end_atom in self._bonds:
                        self._bonds[end_atom].update({start_atom: bond_type})
                    else:
                        self._bonds[end_atom] = {start_atom: bond_type}
                elif end_atom in self._bonds:
                    self._bonds[end_atom].update({start_atom: bond_type})
                    if start_atom in self._bonds:
                        self._bonds[start_atom].update({end_atom: bond_type})
                    else:
                        self._bonds[start_atom] = {end_atom: bond_type}
                else:
                    self._bonds[start_atom] = {end_atom: bond_type}
                    self._bonds[end_atom] = {start_atom: bond_type}
            else:
                raise KeyError('This atoms do not exist')
        else:
            raise TypeError('Arguments should be integers')


__all__ = ['Molecule']
