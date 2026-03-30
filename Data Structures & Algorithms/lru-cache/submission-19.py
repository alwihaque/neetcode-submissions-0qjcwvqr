class LRUCache:
    class Node:
        def __init__(self, key, val, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.hm = {}
        self.capacity = capacity
        self.lru = None
        self.mru = None

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        
        node = self.hm[key]

        # If already MRU or only one node, just return
        if node is self.mru or self.lru is self.mru:
            return node.val
        
        # Remove node from current position
        prev, next = node.prev, node.next
        
        if next:  # Fix: Check if next exists
            next.prev = prev
        
        if prev:
            prev.next = next
        else:  # node was LRU
            self.lru = next
        
        # Move to MRU position
        self.mru.next = node
        node.prev = self.mru
        node.next = None
        self.mru = node
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.hm:
            # Add new node
            node = self.Node(key, value)
            if self.lru is None and self.mru is None:
                self.lru = self.mru = node
            else:
                self.mru.next = node
                node.prev = self.mru
                self.mru = node
            self.hm[key] = node
        else:
            # Update existing node
            node = self.hm[key]
            node.val = value
            
            # Move to MRU if not already there
            if node is not self.mru:
                next, prev = node.next, node.prev
                
                if next:
                    next.prev = prev
                
                if prev:
                    prev.next = next
                else:  # node was LRU
                    self.lru = next
                
                # Move to MRU position
                self.mru.next = node
                node.prev = self.mru
                node.next = None
                self.mru = node
        
        # Evict if over capacity
        if len(self.hm) > self.capacity:
            if self.lru:
                evict = self.lru
                self.lru = evict.next
                if self.lru:
                    self.lru.prev = None
                else:  # Was the only node
                    self.mru = None
                self.hm.pop(evict.key)