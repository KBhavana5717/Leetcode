class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        n = len(num)
        for i in range(min(10, n - 2)):
            if num[0] == '0' and i > 0:
                break
            a = int(num[:i + 1])
            if a > 2**31 - 1:
                break
            for j in range(i + 1, n - 1):
                if num[i + 1] == '0' and j > i + 1:
                    break
                b = int(num[i + 1:j + 1])
                if b > 2**31 - 1:
                    break
                
                fib = [a, b]
                curr = j + 1
                while curr < n:
                    nxt = fib[-1] + fib[-2]
                    if nxt > 2**31 - 1:
                        break
                    nxt_str = str(nxt)
                    if num.startswith(nxt_str, curr):
                        fib.append(nxt)
                        curr += len(nxt_str)
                    else:
                        break
                
                if curr == n and len(fib) >= 3:
                    return fib
                    
        return []