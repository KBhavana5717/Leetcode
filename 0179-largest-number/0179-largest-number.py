from functools import cmp_to_key


class Solution:

  def largestNumber(self, nums: list[int]) -> str:
    # Convert all integers to strings
    str_nums = list(map(str, nums))

    # Custom comparator: compare combinations 'a + b' and 'b + a'
    def compare(a, b):
      if a + b > b + a:
        return -1  # a should come before b
      elif a + b < b + a:
        return 1  # b should come before a
      else:
        return 0

    # Sort using the custom comparator
    str_nums.sort(key=cmp_to_key(compare))

    # Join the sorted numbers into a single string
    result = "".join(str_nums)

    # Handle the edge case where the result is multiple zeros (e.g., [0, 0])
    return "0" if result[0] == "0" else result