class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class MinStack:

    def __init__(self):
        self.head = None
        self.min_head = None

    def push(self, val: int) -> None:
        if self.head is None:
            node = Node(val)
            min_node = Node(val)
            self.head = node
            self.min_head = min_node
            return
        
        node = Node(val)
        min_node = Node(val)
        node.next = self.head
        if min_node.val <= self.min_head.val:
            min_node.next = self.min_head
            self.min_head = min_node
        self.head = node
        

    def pop(self) -> None:
        old_head = self.head
        self.head = self.head.next
        if old_head.val == self.min_head.val:
            self.min_head = self.min_head.next


        
        

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.min_head.val
        
        
