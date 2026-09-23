class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Map each restaurant in list1 to its index
        index_map = {restaurant: i for i, restaurant in enumerate(list1)}
        
        min_sum = float('inf')
        result = []
        
        # Iterate through list2 and check if the restaurant exists in list1
        for j, restaurant in enumerate(list2):
            if restaurant in index_map:
                index_sum = j + index_map[restaurant]
                
                # If we found a smaller index sum, reset the result list
                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [restaurant]
                # If we found another restaurant with the same minimum sum, append it
                elif index_sum == min_sum:
                    result.append(restaurant)
                    
        return result