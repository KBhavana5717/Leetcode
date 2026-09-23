class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Use binary search to find the optimal starting index of the window of size k
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            # Compare the distance of x to arr[mid] vs arr[mid + k]
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
                
        return arr[left:left + k]