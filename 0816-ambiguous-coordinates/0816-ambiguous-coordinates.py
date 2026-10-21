class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        # Strip outer parentheses
        S = s[1:-1]
        
        def make_valid(num_str: str) -> list[str]:
            res = []
            n = len(num_str)
            # Case 1: No decimal point
            # Valid if it doesn't have leading zeros, unless it's just "0"
            if not (n > 1 and num_str[0] == '0'):
                res.append(num_str)
                
            # Case 2: With decimal point
            # Insert decimal point after index i (0 <= i < n - 1)
            for i in range(1, n):
                left, right = num_str[:i], num_str[i:]
                # Left part cannot have leading zeros (unless it's just "0")
                # Right part cannot have trailing zeros
                if (left == '0' or not left.startswith('0')) and not right.endswith('0'):
                    res.append(f"{left}.{right}")
                    
            return res

        ans = []
        # Split string S into two non-empty parts X and Y
        for i in range(1, len(S)):
            X, Y = S[:i], S[i:]
            for x in make_valid(X):
                for y in make_valid(Y):
                    ans.append(f"({x}, {y})")

        return ans