from itertools import zip_longest


class Solution:

  def compareVersion(self, version1: str, version2: str) -> int:
    # Split both version strings by dots into lists of revisions
    v1_parts = version1.split('.')
    v2_parts = version2.split('.')

    # Compare each revision pair side-by-side, padding missing parts with '0'
    for v1, v2 in zip_longest(v1_parts, v2_parts, fillvalue='0'):
      val1, val2 = int(v1), int(v2)

      if val1 < val2:
        return -1
      if val1 > val2:
        return 1

    return 0