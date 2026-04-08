# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_node = ListNode()
        n = dummy_node
        remainder = 0

        while l1 and l2:
            sum_val = (l1.val + l2.val)
             
            val = sum_val % 10
            n.next = ListNode(val + remainder)
            remainder = sum_val // 10

            n = n.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sum_val = (l1.val + remainder)
            print(sum_val)
            val = sum_val % 10
            n.next = ListNode(val)
            remainder = sum_val // 10
            n = n.next
            l1 = l1.next

        
        while l2:
            sum_val = (l2.val + remainder)
            val = sum_val % 10
            n.next = ListNode(val)
            remainder = sum_val // 10
            n = n.next
            l2 = l2.next 

        


        if remainder > 0:
            n.next = ListNode(remainder)
        return dummy_node.next



        