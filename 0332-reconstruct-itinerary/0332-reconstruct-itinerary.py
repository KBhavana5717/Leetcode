from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        
        # Sort tickets in reverse order so we can pop the smallest lexical destination in O(1) time
        tickets.sort(reverse=True)
        for src, dst in tickets:
            graph[src].append(dst)
            
        route = []
        
        def dfs(airport: str):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            route.append(airport)
            
        dfs("JFK")
        
        # Reverse the post-order traversal to get the correct itinerary
        return route[::-1]