class Solution:

  def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    if numerator == 0:
      return '0'

    res = []

    # Handle the sign of the result (negative if signs differ)
    if (numerator < 0) ^ (denominator < 0):
      res.append('-')

    num = abs(numerator)
    den = abs(denominator)

    # Append the integer part
    res.append(str(num // den))
    remainder = num % den

    # If there's no remainder, return the integer result
    if remainder == 0:
      return ''.join(res)

    res.append('.')
    remainder_map = {}

    # Simulate long division to find decimal and repeating parts
    while remainder != 0:
      if remainder in remainder_map:
        res.insert(remainder_map[remainder], '(')
        res.append(')')
        break

      # Record the index of the current remainder
      remainder_map[remainder] = len(res)

      remainder *= 10
      res.append(str(remainder // den))
      remainder %= den

    return ''.join(res)