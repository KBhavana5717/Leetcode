class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 1 has no proper divisors except itself, so it cannot be a perfect number
        if num <= 1:
            return False
            
        total_sum = 1
        i = 2
        
        while i * i <= num:
            if num % i == 0:
                total_sum += i
                # Avoid adding the square root twice if i is the square root
                if i * i != num:
                    total_sum += num // i
            i += 1
            
        return total_sum == num