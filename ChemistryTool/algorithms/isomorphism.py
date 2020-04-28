from typing import Dict
from .abc import IsomorphismABC


class Isomorphism(IsomorphismABC):
    __slots__ = ()

    def get_mapping(self, other) -> Dict[int, int]:
        start, planed_graph, closures = other.plane_graph()
        starts = [(x, y) for x, y in self._atoms.items() if repr(y) == repr(other._atoms[start])]
        for s in starts:
            depth = 1
            stack = [(s[0], a, b, depth) for a, b in self._bonds[s[0]].items()]
            mapping = dict()
            while stack:
                previous, current, bond, depth = stack.pop()

                move = (repr(self._atoms[previous]), repr(self._atoms[current]), bond, depth)
                test = [(repr(other._atoms[p]), repr(other._atoms[c]), b, d) for p, c, b, d in planed_graph]
                if move in test:
                    mapping[previous] = planed_graph[test.index(move)][0]
                    mapping[current] = planed_graph[test.index(move)][1]
                    del planed_graph[test.index(move)]
                else:
                    continue

                depth += 1
                neighbors = [(current, ngb, b, depth) for ngb, b in self._bonds[current].items() if ngb != previous]
                stack.extend(neighbors)
            if not planed_graph:
                return mapping


__all__ = ['Isomorphism']
