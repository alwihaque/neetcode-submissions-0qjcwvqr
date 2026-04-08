# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        length = 0

        while curr:
            curr = curr.next
            length += 1
        
        index_to_remove = length - n
        print(index_to_remove)
        if index_to_remove == 0:
            return head.next
        
        curr = head
        i = 0

        while curr:

            if i == (index_to_remove - 1):
                if curr.next:
                    curr.next = curr.next.next
                else:
                    curr.next = None
            curr = curr.next
            i += 1


        
        
        return head
        
        