# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0 
        res = 0
        dummy = head = ListNode()
        while l1 and l2:
            val = (carry + l1.val + l2.val) % 10 
            carry =  (carry + l1.val + l2.val) // 10
            head.next = ListNode(val)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            val = (carry + l1.val) % 10
            carry = (carry + l1.val) // 10
            head.next = ListNode(val)
            head = head.next
            l1 = l1.next
        
        while l2:
            val = (carry + l2.val) % 10
            carry = (carry + l2.val) // 10
            head.next = ListNode(val)
            head = head.next
            l2 = l2.next
        
        
        if carry == 1:
            head.next = ListNode(1)
        
        return dummy.next
            

        