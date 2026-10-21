class Solution:
    def uniqueLetterString(self, s: str) -> int:
        from collections import defaultdict
        
        index = defaultdict(list)
        for i, char in enumerate(s):
            index[char].append(i)
            
        ans = 0
        for char, arr in index.items():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                ans += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
                
        return ans