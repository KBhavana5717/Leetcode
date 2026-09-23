class Solution:
    def findMaxLength(self, nums):
        prefix_sum = 0
        index_map = {0: -1}   # prefix_sum : first index
        max_len = 0

        for i, num in enumerate(nums):
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in index_map:
                max_len = max(max_len, i - index_map[prefix_sum])
            else:
                index_map[prefix_sum] = i

        return max_len
