# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        h1 = other
        h2 = self

        while h1 is not None and h2 is not None:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next

        return h1 is None and h2 is None

    def as_list(self):
        result = []
        head = self
        while head is not None:
            result.append(head.val)
            head = head.next

        return result

    @staticmethod
    def from_list(values):
        """
        :type values: [String]
        :return ListNode:
        """
        head = tail = None
        for val in values:
            node = ListNode(val)
            if head is None:
                head = node
            else:
                tail.next = node
            tail = node

        return head

    def __str__(self):
        return str(self.val)
