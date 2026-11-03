class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_counts = {0: 1}
        
        for num in nums:
            prefix_sum += num
            rem = prefix_sum % k
            if rem < 0:
                rem += k
            if rem in remainder_counts:
                count += remainder_counts[rem]
                remainder_counts[rem] += 1
            else:
                remainder_counts[rem] = 1
                
        return count