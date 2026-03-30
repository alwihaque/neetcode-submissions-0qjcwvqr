# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []

        node = head

        while node and node not in visited:
            
            visited.append(node)
            node = node.next
        
        return node is not None
        