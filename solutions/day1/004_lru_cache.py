"""
146 LRU Cache
https://leetcode.com/problems/lru-cache/

Time Complexity: O(1) for both get and put operations
Space Complexity: O(capacity) - We store at most capacity elements
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize LRU cache with given capacity.
        
        Args:
            capacity: int - Maximum number of items the cache can hold
        """
        self.capacity = capacity
        self.cache = {}  # Map key to node for O(1) lookup
        
        # Create dummy head and tail nodes for easier edge case handling
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        """
        Remove a node from the linked list.
        
        Args:
            node: Node - The node to remove
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add(self, node):
        """
        Add a node right before the tail (most recently used position).
        
        Args:
            node: Node - The node to add
        """
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
    
    def get(self, key: int) -> int:
        """
        Get the value of the key if it exists in the cache, otherwise return -1.
        Also moves the accessed item to the most recently used position.
        
        Args:
            key: int - The key to look up
            
        Returns:
            int - The value associated with the key, or -1 if not found
        """
        if key in self.cache:
            node = self.cache[key]
            # Move accessed node to MRU position
            self._remove(node)
            self._add(node)
            return node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        """
        Insert or update the value of the key.
        If the cache reaches capacity, it should invalidate the least recently used item.
        
        Args:
            key: int - The key to insert or update
            value: int - The value to associate with the key
        """
        if key in self.cache:
            # Key exists, update value and move to MRU
            self._remove(self.cache[key])
        
        # Create new node and add to cache
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add(new_node)
        
        # Check if we exceed capacity
        if len(self.cache) > self.capacity:
            # Remove LRU item (node right after head)
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

# Test the solution
if __name__ == "__main__":
    # Test case from LeetCode example
    cache = LRUCache(2)
    
    cache.put(1, 1)
    cache.put(2, 2)
    print("get(1):", cache.get(1))  # returns 1
    cache.put(3, 3)                 # evicts key 2
    print("get(2):", cache.get(2))  # returns -1 (not found)
    cache.put(4, 4)                 # evicts key 1
    print("get(1):", cache.get(1))  # returns -1 (not found)
    print("get(3):", cache.get(3))  # returns 3
    print("get(4):", cache.get(4))  # returns 4