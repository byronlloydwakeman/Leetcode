from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Completed 16/04/2024 as a daily challenge

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        num = 0

        # Recursion function so it can keep looping back on itself
        def recursion(root, path, pathLen):
            # Doesn't like global variables to be changed in a local state
            nonlocal num
            # Reached the end of the leaf
            if root is None:
                return

            # Checks if there are values beyond the pathLen, if so overwrite them else append them
            if len(path) > pathLen:
                path[pathLen] = root.val
            else:
                path.append(root.val)

            pathLen += 1

            if root.left is None and root.right is None:
                str_num = ""
                for p in path[:pathLen]:  # Only consider elements up to pathLen
                    str_num += str(p)
                num += int(str_num)

            else:
                recursion(root.left, path, pathLen)  # Pass pathLen + 1 to recursive calls
                recursion(root.right, path, pathLen)

            # Reset pathLen after each recursive call
            pathLen -= 1

        path = []
        recursion(root, path, 0)

        return num
