# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First iteration returns None
        if not head:
            print("first")
            return None

        # Store a temp value
        temp = head

        # The end of the arrays greatest value
        greater = self.removeNodes(temp.next)
        # Add the next greater value
        temp.next = greater
        # Check its not None or that the new value is greater than the current greatest
        if not greater or temp.val >= greater.val:
            return temp
        else:
            return greater
        
