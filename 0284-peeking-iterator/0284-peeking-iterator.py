class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        # Cache the next element, or set to None if iterator is empty
        self._next_element = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        return self._next_element

    def next(self):
        res = self._next_element
        # Advance the iterator and update the cache
        self._next_element = self.iterator.next() if self.iterator.hasNext() else None
        return res

    def hasNext(self):
        return self._next_element is not None