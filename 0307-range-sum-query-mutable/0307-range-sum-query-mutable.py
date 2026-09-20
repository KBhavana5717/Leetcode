class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        
        # Populate the Fenwick tree
        for i, num in enumerate(nums):
            self._add(i + 1, num)

    def _add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def _query(self, i: int) -> int:
        sum_val = 0
        while i > 0:
            sum_val += self.tree[i]
            i -= i & (-i)
        return sum_val

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, diff)

    def sumRange(self, left: int, right: int) -> int:
        return self._query(right + 1) - self._query(left)