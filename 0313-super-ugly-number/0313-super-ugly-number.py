class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        # dp array to store the first n super ugly numbers
        ugly = [1] * n
        # Pointers for each prime
        pointers = [0] * len(primes)
        # Current values for each prime multiplier
        values = list(primes)
        
        for i in range(1, n):
            next_ugly = min(values)
            ugly[i] = next_ugly
            
            # Update pointers and values
            for j in range(len(primes)):
                if values[j] == next_ugly:
                    pointers[j] += 1
                    values[j] = ugly[pointers[j]] * primes[j]
                    
        return ugly[n - 1]