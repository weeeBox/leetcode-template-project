from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return '{} ({}, {})'.format(self.val, self.left.val if self.left is not None else '?',
                                    self.right.val if self.right is not None else '?')

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        def eq(a: TreeNode, b: TreeNode) -> bool:
            return not a and not b or a and b and a.val == b.val and eq(a.left, b.left) and eq(a.right, b.right)
        return eq(self, other)

    def find(self, val):
        queue = [self]
        while queue:
            node = queue.pop()
            if node.val == val:
                return node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return None

    @staticmethod
    def from_list(values):
        if len(values) == 0:
            return None

        root = TreeNode(values[0])
        q = deque()
        q.append(root)
        i = 1
        while len(q) > 0:
            node = q.popleft()
            if i == len(values):
                break

            val = values[i]
            i = i + 1

            if val != 'null':
                node.left = TreeNode(int(val))
                q.append(node.left)

            if i == len(values):
                break

            val = values[i]
            i = i + 1

            if val != 'null':
                node.right = TreeNode(int(val))
                q.append(node.right)

        return root
