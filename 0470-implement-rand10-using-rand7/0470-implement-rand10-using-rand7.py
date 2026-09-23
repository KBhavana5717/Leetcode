class Solution:
    def rand10(self) -> int:
        while True:
            # Generate a uniform random number from 1 to 49
            idx = (rand7() - 1) * 7 + rand7()
            
            # If the number is within 1 to 40, map it to 1-10
            if idx <= 40:
                return 1 + (idx - 1) % 10