# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def traverseTree(root):
            # At the leaf
            if not root.left and not root.right:
                return root.val
            # Carry on the search for the left and right branches
            left_boolean = traverseTree(root.left)
            right_boolean = traverseTree(root.right)
            return left_boolean and right_boolean if root.val == 3 else left_boolean or right_boolean
        
        return traverseTree(root)
        
        
