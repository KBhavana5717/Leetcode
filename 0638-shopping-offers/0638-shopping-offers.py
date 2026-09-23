class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        memo = {}

        def dfs(curr_needs):
            # Check if state is already computed
            tuple_needs = tuple(curr_needs)
            if tuple_needs in memo:
                return memo[tuple_needs]
            
            # Base cost: buying all remaining items individually at regular price
            res = sum(curr_needs[i] * price[i] for i in range(len(curr_needs)))
            
            # Try using each special offer
            for offer in special:
                valid = True
                next_needs = list(curr_needs)
                
                # Check if the offer can be applied without exceeding current needs
                for i in range(len(curr_needs)):
                    next_needs[i] -= offer[i]
                    if next_needs[i] < 0:
                        valid = False
                        break
                
                # If valid, recursively find the minimum cost with the updated needs
                if valid:
                    res = min(res, offer[-1] + dfs(next_needs))
                    
            memo[tuple_needs] = res
            return res

        return dfs(needs)