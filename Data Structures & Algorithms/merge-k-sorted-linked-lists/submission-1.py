# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def merge(self, head1, head2):
        print(head2.val)
        dummy_node = ListNode()
        curr = dummy_node
        while head1 and head2:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        
        curr.next = head1 if head1 else head2
        return dummy_node.next

    def divide(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]
        m = l + (r - l) // 2
        left = self.divide(lists, l, m)
        right = self.divide(lists, m + 1, r)
        return self.merge(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        return self.divide(lists, 0, len(lists) - 1)
        
        
        
        