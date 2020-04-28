from typing import Tuple

from .abc import MoleculeABC
from ..algorithms import Isomorphism
from ..periodictable.element import Element


class Molecule(Isomorphism, MoleculeABC):
    __slots__ = ()

    def add_atom(self, element: Element, number: int):
        if isinstance(element, Element) and isinstance(number, int):
            if number in self._atoms:
                raise KeyError('This atom already exists')
            else:
                self._atoms[number] = element
                self._bonds[number] = {}
                element.attach(self, number)

        else:
            raise TypeError

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if start_atom in self._atoms and end_atom in self._atoms:
            if start_atom == end_atom:
                raise KeyError('Atoms should be different')
            elif end_atom in self._bonds[start_atom]:
                raise KeyError('This bond already exists')
            else:
                self._bonds[start_atom][end_atom] = self._bonds[end_atom][start_atom] = bond_type
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
        if self._atoms[number]:
            if isinstance(element, Element):
                self._atoms[number] = element
            else:
                raise TypeError
        else:
            raise KeyError('This atom is not exist')

    def update_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if self._bonds[start_atom][end_atom]:
            self._bonds[start_atom][end_atom] = self._bonds[end_atom][start_atom] = bond_type
        else:
            raise KeyError('This bond is not exist')

    def __enter__(self):
        self._backup_atoms = self._atoms.copy()
        self._backup_bonds = {x.copy(): y.copy() for x, y in self._atoms.items()}
        return self._atoms, self._bonds

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self._atoms = self._backup_atoms
            self._bonds = self._backup_bonds
            del self._backup_atoms
            del self._backup_bonds
        else:
            del self._backup_atoms
            del self._backup_bonds

    def __str__(self):
        s = ''
        for a in set(self._atoms.values()):
            s += f'{a}{list(self._atoms.values()).count(a)}'
        return s

    def plane_graph(self):
        bonds = self._bonds
        start = 1
        seen = {start}
        depth = 1
        stack = [(start, m, b, depth) for m, b in bonds[start].items()]
        path = []
        closures = []
        while stack:
            previous, current, bond, d = move = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            path.append(move)
            depth += 1
            for m, b in bonds[current].items():
                if m == previous:
                    continue
                elif m in seen:
                    closures.append((m, current, b, depth))
                else:
                    stack.append((current, m, b, depth))
        return start, path, closures


    @property
    def connected_components(self) -> Tuple[Tuple[int, ...], ...]:
        pass

    @property
    def connected_components_count(self) -> int:
        pass

    @property
    def rings_count(self) -> int:
        pass


__all__ = ['Molecule']
