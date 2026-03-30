# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        slow, fast = first, first.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next

        slow.next = None

        # reverse second list
        prev_node = None
        while second:
            node = second
            second = second.next
            node.next = prev_node
            prev_node = node
        
        while first and prev_node:
            first_next = first.next
            second_next = prev_node.next
            first.next = prev_node
            prev_node.next = first_next
            first = first_next
            prev_node = second_next

        
        
        
        