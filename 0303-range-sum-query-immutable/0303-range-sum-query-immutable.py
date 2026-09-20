class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = []
        current_sum = 0
        for num in nums:
            current_sum += num
            self.prefix.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix[right]
        left_sum = self.prefix[left - 1] if left > 0 else 0
        return right_sum - left_sum