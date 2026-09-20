class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
            
        bucket_size = valueDiff + 1
        buckets = {}
        
        for i, num in enumerate(nums):
            bucket_id = num // bucket_size
            
            # Check if the same bucket already has a number
            if bucket_id in buckets:
                return True
                
            # Check the left neighboring bucket
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
                
            # Check the right neighboring bucket
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
                
            # Place the current number into its bucket
            buckets[bucket_id] = num
            
            # Maintain the window size of indexDiff
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // bucket_size
                del buckets[old_bucket_id]
                
        return False