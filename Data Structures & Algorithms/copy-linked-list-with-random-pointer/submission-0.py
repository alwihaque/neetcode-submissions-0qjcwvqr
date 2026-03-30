"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        
        # two pass through the list 
        
        head_prev = Node(0)
        new_head = head_prev

        node = head
        hm = {}

        while node:
            new_head.next = Node(node.val)
            hm[node] = new_head.next
            node = node.next
            new_head = new_head.next
            

        node = head
        node2 = head_prev.next
        while node:
            random = node.random
            if random is not None:
                random_copy = hm[random]
            else:
                random_copy = None
            node2.random = random_copy
            node = node.next
            node2 = node2.next

        


        return head_prev.next
            

        
            

        
        
        