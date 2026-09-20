class Solution:

  def convertToTitle(self, columnNumber: int) -> str:
    res = []

    while columnNumber > 0:
      # Adjust columnNumber to 1-based indexing equivalent for 26-base conversion
      columnNumber -= 1
      remainder = columnNumber % 26
      res.append(chr(ord('A') + remainder))
      columnNumber //= 26

    # Reverse since we extract characters from right to left
    return ''.join(reversed(res))