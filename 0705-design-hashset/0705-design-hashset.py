class MyHashSet:

    def __init__(self):
        self.key_range = 769
        self.bucket = [[] for _ in range(self.key_range)]

    def _hash(self, key: int) -> int:
        return key % self.key_range

    def add(self, key: int) -> None:
        bucket_index = self._hash(key)
        if key not in self.bucket[bucket_index]:
            self.bucket[bucket_index].append(key)

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        if key in self.bucket[bucket_index]:
            self.bucket[bucket_index].remove(key)

    def contains(self, key: int) -> bool:
        bucket_index = self._hash(key)
        return key in self.bucket[bucket_index]