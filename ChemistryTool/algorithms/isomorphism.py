from typing import Dict
from .abc import IsomorphismABC


class Isomorphism(IsomorphismABC):
    __slots__ = ()

    def get_mapping(self, other) -> Dict[int, int]:
        start, planed_graph, closures = self.plane_graph(other)
        starts = [(x, y) for x, y in self._atoms.items() if y == other._atoms[start]]
        for s in starts:
            depth = 1
            stack = [(s[0], a, b, depth) for a, b in self._bonds[s[0]].items()]
            mapping = dict()
            while stack:
                previous, current, bond, depth = stack.pop()

                move = (self._atoms[previous], self._atoms[current], bond, depth)
                test = [(other._atoms[p], other._atoms[c], b, d) for p, c, b, d in planed_graph]
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

    def plane_graph(self, other):
        bonds = other._bonds
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


__all__ = ['Isomorphism']
