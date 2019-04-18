from typing import List
from unittest import TestCase

from list_node import ListNode
from tree_node import TreeNode
from tree_link_node import TreeLinkNode
from Interval import Interval

from solution import Solution

null = 'null'


class TestSolution(TestCase):
    def test_1(self):
        self.assertEqual(3, Solution().sumNumbers(1, 2))
