class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)

        # The answer has between 2 and 60 digits (since base 2 gives the
        # longest representation, and 2^59 > 10^18).
        # Try decreasing digit-lengths m; for each m, binary search the base k
        # such that 1 + k + k^2 + ... + k^(m-1) == num.
        max_m = num.bit_length()  # upper bound on possible digit count (base 2 case)

        for m in range(max_m, 1, -1):
            k = self.find_base(num, m)
            if k is not None:
                return str(k)

        # Fallback: base (num - 1) always works, representation "11"
        return str(num - 1)

    def find_base(self, num, m):
        # Binary search for integer k >= 2 such that sum_{i=0}^{m-1} k^i == num
        low, high = 2, int(num ** (1.0 / (m - 1))) + 1

        while low <= high:
            mid = (low + high) // 2
            total = self.geo_sum(mid, m, num)
            if total == num:
                return mid
            elif total < num:
                low = mid + 1
            else:
                high = mid - 1

        return None

    def geo_sum(self, k, m, cap):
        # Computes 1 + k + k^2 + ... + k^(m-1), stopping early if it exceeds cap
        total = 0
        cur = 1
        for _ in range(m):
            total += cur
            if total > cap:
                return total
            cur *= k
        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestGoodBase("13"))    # "3"
    print(sol.smallestGoodBase("4681"))  # "8"
    print(sol.smallestGoodBase("1000000000000000000"))  # "999999999999999999"