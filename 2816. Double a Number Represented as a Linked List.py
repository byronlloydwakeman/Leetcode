# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     head = None
    # def insertAtEnd(self, data):
    #     new_node = ListNode(data)
    #     if self.head is None:
    #         self.head = new_node
    #         return
    
    #     current_node = self.head
    #     while(current_node.next):
    #         current_node = current_node.next
    
    #     current_node.next = new_node

#     def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         sys.set_int_max_str_digits(100000)
        # nums = []
        # def recursion(new_head):
        #     if new_head == None or new_head.val == None:
        #         return
        #     nums.append(new_head.val)
        #     recursion(new_head.next)

#         recursion(head)
#         str_num_1_list = []
#         for num in nums:
#             str_num_1_list.append(str(num))

#         str_int_num_1 = "".join(str_num_1_list) # First num as a str
#         to_return = int(str_int_num_1) * 2 # Second num as a num

#         str_num_2_list = list(str(to_return))# Second num as a str array

#         for num in str_num_2_list:
#             self.insertAtEnd(num)

#         return self.head

# Same solution but time optimized
class Solution:
    def __init__(self):
        self.reversed = None
        self.reversed_double = None

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(100000) # There are some test cases which convert str to int and vice versa using large values
        if not head:
            return None

        # Convert the linked list into its str equiv
        def list_to_str(head):
            str_num = ""
            current_node = head
            while current_node:
                str_num += str(current_node.val)
                current_node = current_node.next
            return str_num

        # Create a linked list from a str
        def str_to_linked_list(str_num):
            dummy = ListNode()
            current_node = dummy
            for char in str_num:
                current_node.next = ListNode(int(char))
                current_node = current_node.next
            return dummy.next

        # Convert the linked list to its str representation, double it, and then convert back to linked list
        # Linked list -> str representtion
        # Double it -> Linked list
        str_num = list_to_str(head)
        doubled_str = str(int(str_num) * 2)
        return str_to_linked_list(doubled_str)


        
