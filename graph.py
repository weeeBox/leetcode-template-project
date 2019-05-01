# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

    def __repr__(self):
        return str(self.val) + ' (' + ', '.join(str(n.val) for n in self.neighbors) + ')'

    @classmethod
    def from_dict(cls, data):
        return cls.__from_dict(data, {})

    @classmethod
    def __from_dict(cls, data, lookup):
        identifier = data.get('$id', None)
        if identifier:
            node = Node(data['val'], [])
            lookup[identifier] = node
            for neighbor_data in data['neighbors']:
                neighbor = cls.__from_dict(neighbor_data, lookup)
                node.neighbors.append(neighbor)
            return node

        return lookup[data['$ref']]
