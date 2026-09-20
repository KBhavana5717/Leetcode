class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def helper(house_sublist):
            rob1, rob2 = 0, 0
            for n in house_sublist:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        # Return the maximum of robbing from house 0 to n-2 OR house 1 to n-1
        return max(helper(nums[:-1]), helper(nums[1:]))     