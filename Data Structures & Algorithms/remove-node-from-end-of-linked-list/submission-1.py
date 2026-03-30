# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        node = head
        while node:
            N += 1
            node = node.next
        
        node_to_remove = N - n
        if node_to_remove == 0:
            return head.next

        curr = head
        
        for i in range(N - 1):
            if (i + 1) == node_to_remove:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head

            
        