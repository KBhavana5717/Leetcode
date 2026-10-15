class MapSum:

    def __init__(self):
        self.map = {}
        self.prefix_sum = collections.defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map.get(key, 0)
        self.map[key] = val
        for i in range(1, len(key) + 1):
            self.prefix_sum[key[:i]] += diff

    def sum(self, prefix: str) -> int:
        return self.prefix_sum[prefix]