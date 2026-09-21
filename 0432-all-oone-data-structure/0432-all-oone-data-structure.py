class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.head = Node(0)  # Sentinel head (smaller counts)
        self.tail = Node(0)  # Sentinel tail (larger counts)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_count = {}   # Map: key -> count
        self.count_node = {}  # Map: count -> Node

    def _add_node_after(self, new_node, prev_node):
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node
        self.count_node[new_node.count] = new_node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.count_node[node.count]

    def inc(self, key: str) -> None:
        if key in self.key_count:
            count = self.key_count[key]
            self.key_count[key] = count + 1
            curr_node = self.count_node[count]
            curr_node.keys.remove(key)
            
            next_count = count + 1
            if next_count in self.count_node:
                self.count_node[next_count].keys.add(key)
            else:
                new_node = Node(next_count)
                new_node.keys.add(key)
                self._add_node_after(new_node, curr_node)
            
            if not curr_node.keys:
                self._remove_node(curr_node)
        else:
            self.key_count[key] = 1
            if 1 in self.count_node:
                self.count_node[1].keys.add(key)
            else:
                new_node = Node(1)
                new_node.keys.add(key)
                self._add_node_after(new_node, self.head)

    def dec(self, key: str) -> None:
        count = self.key_count[key]
        curr_node = self.count_node[count]
        curr_node.keys.remove(key)
        
        if count == 1:
            del self.key_count[key]
        else:
            self.key_count[key] = count - 1
            prev_count = count - 1
            if prev_count in self.count_node:
                self.count_node[prev_count].keys.add(key)
            else:
                new_node = Node(prev_count)
                new_node.keys.add(key)
                self._add_node_after(new_node, curr_node.prev)
        
        if not curr_node.keys:
            self._remove_node(curr_node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))