# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # At the end
        if node is None or node.next is None:
            return

        # Effecetively delete the value by replacing it with the next value
        node.val = node.next.val

        node.next = node.next.next

                
