class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_valid(string, i):
            skip = 0
            while i >= 0:
                if string[i] == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    return i
                i -= 1
            return -1

        i, j = len(s) - 1, len(t) - 1
        while True:
            i = next_valid(s, i)
            j = next_valid(t, j)

            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0:
                return False
            if s[i] != t[j]:
                return False

            i -= 1
            j -= 1