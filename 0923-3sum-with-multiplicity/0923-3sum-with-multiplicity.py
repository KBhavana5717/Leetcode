from collections import Counter

class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        MOD = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count.keys())
        res = 0
        
        n = len(keys)
        for i in range(n):
            for j in range(i, n):
                k = target - keys[i] - keys[j]
                if k < keys[j]:
                    continue
                if k in count:
                    if keys[i] == keys[j] == k:
                        res += count[keys[i]] * (count[keys[i]] - 1) * (count[keys[i]] - 2) // 6
                    elif keys[i] == keys[j]:
                        res += count[keys[i]] * (count[keys[i]] - 1) // 2 * count[k]
                    elif keys[j] == k:
                        res += count[keys[i]] * count[keys[j]] * (count[keys[j]] - 1) // 2
                    else:
                        res += count[keys[i]] * count[keys[j]] * count[k]
                        
        return res % MOD