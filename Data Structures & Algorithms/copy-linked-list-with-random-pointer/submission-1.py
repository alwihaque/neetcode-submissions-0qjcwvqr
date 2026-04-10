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
        dummy_node = Node('0')
        mapping = {}
        mapping_2 = {}

        node, curr = dummy_node, head
        while curr:
            node.next = Node(curr.val)
            mapping[curr] = node.next
            mapping_2[node.next] = curr
            curr = curr.next
            node = node.next
        
        node = dummy_node.next
        while node:
            original_node = mapping_2[node]
            original_random = original_node.random
            if original_random:
                clone_random = mapping[original_random]
                node.random = clone_random
            else:
                node.random = None
            
            node = node.next
        
        return dummy_node.next
        

        

            
        return dummy_node.next
