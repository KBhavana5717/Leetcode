class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1

        # s holds the magical string itself, built incrementally.
        # Seed with the known start: "122"
        s = [1, 2, 2]
        # i is the pointer into s telling us which group-length we're generating next.
        # We already "used" s[0]=1 and s[1]=2 to produce the seed, so start at index 2.
        i = 2
        # The next character to append alternates between 1 and 2.
        next_char = 1

        while len(s) < n:
            count = s[i]          # how many times to repeat next_char
            s.extend([next_char] * count)
            next_char = 3 - next_char  # toggle between 1 and 2
            i += 1

        return s[:n].count(1)