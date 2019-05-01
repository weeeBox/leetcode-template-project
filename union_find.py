class UnionFind:
    def __init__(self, n: int):
        self.array = [-1] * n

    def union(self, p: int, q: int) -> None:
        p = self.find(p)
        q = self.find(q)

        if p != q:
            if self.array[p] <= self.array[q]:
                self.array[p] += self.array[q]
                self.array[q] = p
            else:
                self.array[q] += self.array[p]
                self.array[p] = q

    def find(self, p: int) -> int:
        if self.array[p] < 0:
            return p

        # find root
        parent = self.array[p]
        while self.array[parent] >= 0:
            parent = self.array[parent]

        # flatten path
        while self.array[p] >= 0:
            self.array[p], p = parent, self.array[p]

        return p

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def connected_components(self) -> int:
        count = 0
        for x in self.array:
            count += 1 if x < 0 else 0
        return count

    def path(self, p):
        path = []
        while self.array[p] >= 0:
            path.append(p)
            p = self.array[p]

        path.append(p)
        return '->'.join(str(x) for x in path)
