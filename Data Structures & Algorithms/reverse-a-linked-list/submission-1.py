# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = None
        node = head

        while node:
            prev = dummy_node
            dummy_node = node
            node = node.next
            dummy_node.next = prev
        
        return dummy_node
        
        