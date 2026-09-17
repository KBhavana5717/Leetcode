class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in (num1, num2):
            return "0"
            
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                
                product = digit1 * digit2
                p1, p2 = i + j, i + j + 1
                
                # Sum the product with existing value and handle carry
                total = product + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10
                
        # Convert result array to string and remove leading zeros
        ans = "".join(map(str, res))
        return ans.lstrip("0")