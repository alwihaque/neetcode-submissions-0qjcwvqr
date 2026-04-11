class Node:
    def __init__(self, key: int, value: int):
        self.key, self.val = key, value
        self.prev, self.next = None, None



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def add(self,node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        
        new_node = Node(key, value)
        self.add(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
            
        
