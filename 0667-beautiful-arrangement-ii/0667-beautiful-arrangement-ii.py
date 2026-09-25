class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        ans = []
        low, high = 1, k + 1
        
        # Alternate between low and high for the first k + 1 elements
        for i in range(k + 1):
            if i % 2 == 0:
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1
                
        # Append the remaining numbers sequentially from k + 2 to n
        for i in range(k + 2, n + 1):
            ans.append(i)
            
        return ans