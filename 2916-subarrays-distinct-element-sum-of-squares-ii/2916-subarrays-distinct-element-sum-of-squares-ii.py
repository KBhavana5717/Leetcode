class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.sum_val = [0] * (4 * n)

    def _push(self, node, l, r):
        if self.lazy[node] != 0:
            val = self.lazy[node]
            mid = (l + r) // 2
            
            # Update left child
            self.sum_val[2 * node] = (self.sum_val[2 * node] + 2 * val * self.tree[2 * node] + val * val * (mid - l + 1)) % 1000000007
            self.tree[2 * node] = (self.tree[2 * node] + val * (mid - l + 1)) % 1000000007
            self.lazy[2 * node] = (self.lazy[2 * node] + val) % 1000000007
            
            # Update right child
            self.sum_val[2 * node + 1] = (self.sum_val[2 * node + 1] + 2 * val * self.tree[2 * node + 1] + val * val * (r - mid)) % 1000000007
            self.tree[2 * node + 1] = (self.tree[2 * node + 1] + val * (r - mid)) % 1000000007
            self.lazy[2 * node + 1] = (self.lazy[2 * node + 1] + val) % 1000000007
            
            self.lazy[node] = 0

    def update(self, node, l, r, ql, qr, val):
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            self.sum_val[node] = (self.sum_val[node] + 2 * val * self.tree[node] + val * val * (r - l + 1)) % 1000000007
            self.tree[node] = (self.tree[node] + val * (r - l + 1)) % 1000000007
            self.lazy[node] = (self.lazy[node] + val) % 1000000007
            return
        
        self._push(node, l, r)
        mid = (l + r) // 2
        self.update(2 * node, l, mid, ql, qr, val)
        self.update(2 * node + 1, mid + 1, r, ql, qr, val)
        
        self.tree[node] = (self.tree[2 * node] + self.tree[2 * node + 1]) % 1000000007
        self.sum_val[node] = (self.sum_val[2 * node] + self.sum_val[2 * node + 1]) % 1000000007

    def query_sum(self):
        return self.sum_val[1]

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        seg = SegmentTree(n)
        last_occurrence = {}
        total_sum = 0
        
        for j in range(n):
            x = nums[j]
            prev_idx = last_occurrence.get(x, -1)
            # Update range [prev_idx + 1, j] by adding 1
            seg.update(1, 0, n - 1, prev_idx + 1, j, 1)
            last_occurrence[x] = j
            
            total_sum = (total_sum + seg.query_sum()) % MOD
            
        return total_sum