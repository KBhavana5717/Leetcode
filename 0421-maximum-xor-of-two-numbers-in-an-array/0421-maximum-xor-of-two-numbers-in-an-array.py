class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        max_xor = 0
        mask = 0
        
        # Iterate from the most significant bit (31st bit) down to 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            # Find all prefix prefixes for the current mask
            prefixes = {num & mask for num in nums}
            
            # Assume the i-th bit of the maximum XOR can be 1
            candidate = max_xor | (1 << i)
            
            # Check if there exist two prefixes p1 and p2 such that p1 ^ p2 == candidate
            # Mathematically, this is equivalent to checking if candidate ^ p1 exists in prefixes
            for p in prefixes:
                if (candidate ^ p) in prefixes:
                    max_xor = candidate
                    break
                    
        return max_xor