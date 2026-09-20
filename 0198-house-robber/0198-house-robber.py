class Solution:

  def rob(self, nums: list[int]) -> int:
    if not nums:
      return 0
    if len(nums) == 1:
      return nums[0]

    # Initialize variables to keep track of the maximum money robbed up to the previous two houses
    prev2 = 0  # Max money up to i-2 houses
    prev1 = 0  # Max money up to i-1 houses

    for num in nums:
      # Current max is either robbing the current house + prev2, or skipping it (prev1)
      current = max(prev1, prev2 + num)
      prev2 = prev1
      prev1 = current

    return prev1