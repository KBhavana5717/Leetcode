class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Initialize a list of boolean values for numbers 0 to n-1
        primes = [True] * n
        primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
        
        # Iterate from 2 up to the square root of n
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                # Mark multiples of i as not prime, starting from i * i
                for j in range(i * i, n, i):
                    primes[j] = False
                    
        return sum(primes)  