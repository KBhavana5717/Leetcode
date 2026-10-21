class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Sentinels: an 'L' at the start and an 'R' at the end
        # don't change anything, but remove edge-case handling.
        s = "L" + dominoes + "R"
        res = list(s)

        p1 = 0
        for p2 in range(1, len(s)):
            if s[p2] == '.':
                continue

            s1, s2 = s[p1], s[p2]

            if s1 == s2:                      # L...L or R...R
                for j in range(p1 + 1, p2):
                    res[j] = s1
            elif s1 == 'R' and s2 == 'L':     # R...L, meet in the middle
                length = p2 - p1 - 1
                for j in range(1, length // 2 + 1):
                    res[p1 + j] = 'R'
                    res[p2 - j] = 'L'
                # if length is odd, the middle stays '.'
            # L...R: everything in between stays '.'

            p1 = p2

        return "".join(res[1:-1])             # strip the sentinels