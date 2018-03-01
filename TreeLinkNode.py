# Definition for binary tree with next pointer.
from collections import deque


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __str__(self):
        return '{} ({}, {}) {}'.format(
            self.val,
            self.left.val if self.left is not None else '?',
            self.right.val if self.right is not None else '?',
            self.next.val if self.next is not None else '?'
        )

    @staticmethod
    def from_list(values):
        if len(values) == 0:
            return None

        root = TreeLinkNode(values[0])
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
                node.left = TreeLinkNode(int(val))
                q.append(node.left)

            if i == len(values):
                break

            val = values[i]
            i = i + 1

            if val != 'null':
                node.right = TreeLinkNode(int(val))
                q.append(node.right)

        return root
