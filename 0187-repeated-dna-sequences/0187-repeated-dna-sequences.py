class Solution:

  def findRepeatedDnaSequences(self, s: str) -> list[str]:
    seen = set()
    repeated = set()

    # Iterate through all 10-letter-long substrings
    for i in range(len(s) - 9):
      sub = s[i : i + 10]
      if sub in seen:
        repeated.add(sub)
      else:
        seen.add(sub)

    return list(repeated)