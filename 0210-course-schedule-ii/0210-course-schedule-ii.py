class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Build the adjacency list
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
            
        # Track visit states: 0 = unvisited, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        result = []
        
        def dfs(course):
            if visited[course] == 1:
                return False  # Cycle detected
            if visited[course] == 2:
                return True   # Already processed
            
            visited[course] = 1  # Mark as currently visiting
            
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
                    
            visited[course] = 2  # Mark as fully visited
            result.append(course)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []  # Return empty array if a cycle is found
                
        return result