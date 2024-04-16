# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(
            self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val=val, left=root)
            return new_root

        self._addRow(root, val, depth, 1)
        return root

    def _addRow(
            self, node: Optional[TreeNode], val: int, depth: int, current_depth: int
    ) -> None:
        if node is None:
            return

        if current_depth == depth - 1:
            new_left = TreeNode(val=val, left=node.left)
            new_right = TreeNode(val=val, right=node.right)
            node.left = new_left
            node.right = new_right
        else:
            self._addRow(node.left, val, depth, current_depth + 1)
            self._addRow(node.right, val, depth, current_depth + 1)
