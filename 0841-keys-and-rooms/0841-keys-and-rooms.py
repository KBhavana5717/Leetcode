class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        stack = [0]
        visited.add(0)
        
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
                    
        return len(visited) == len(rooms)