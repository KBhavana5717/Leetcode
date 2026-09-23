class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # Helper functions to count single and two-character decodings
        def check_one(ch):
            if ch == '*':
                return 9
            if ch == '0':
                return 0
            return 1

        def check_two(c1, c2):
            if c1 == '*' and c2 == '*':
                return 15  # '11'-'19' (9) + '21'-'26' (6)
            if c1 == '*':
                # c2 is a digit '0'-'9'
                if c2 <= '6':
                    return 2  # e.g., '*2' can be '12' or '22'
                else:
                    return 1  # e.g., '*7' can only be '17'
            if c2 == '*':
                # c1 is a digit '1' or '2'
                if c1 == '1':
                    return 9  # '11'-'19'
                elif c1 == '2':
                    return 6  # '21'-'26'
                else:
                    return 0
            
            # Both are normal digits
            val = int(c1) * 10 + int(c2)
            return 1 if 10 <= val <= 26 else 0

        # DP variables representing ways to decode up to i-1 and i-2
        e2 = 1  # ways for empty string
        e1 = check_one(s[0])  # ways for first character
        
        for i in range(1, len(s)):
            current = (e1 * check_one(s[i]) + e2 * check_two(s[i-1], s[i])) % MOD
            e2 = e1
            e1 = current
            
        return e1