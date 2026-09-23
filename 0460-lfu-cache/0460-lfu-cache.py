class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_node(self, node):
        # Add right after head (most recently used for this frequency)
        p = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = p
        p.prev = node
        self.size += 1

    def remove_node(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        self.size -= 1

    def pop_tail(self):
        # Pop the least recently used node from this frequency list (just before tail)
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove_node(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_node = {}
        self.freq_to_group = {}

    def _update_freq(self, node):
        freq = node.freq
        self.freq_to_group[freq].remove_node(node)
        
        if freq == self.min_freq and self.freq_to_group[freq].size == 0:
            self.min_freq += 1
            
        node.freq += 1
        if node.freq not in self.freq_to_group:
            self.freq_to_group[node.freq] = DoublyLinkedList()
        self.freq_to_group[node.freq].add_node(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._update_freq(node)
        else:
            if len(self.key_to_node) >= self.capacity:
                # Evict LFU and LRU tie-breaker
                lfu_list = self.freq_to_group[self.min_freq]
                to_remove = lfu_list.pop_tail()
                del self.key_to_node[to_remove.key]
                
            # Insert new node
            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            self.min_freq = 1
            if 1 not in self.freq_to_group:
                self.freq_to_group[1] = DoublyLinkedList()
            self.freq_to_group[1].add_node(new_node)