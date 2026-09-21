class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        # Sort people: tallest first by height (descending), 
        # and if heights are equal, by smaller k-value first (ascending)
        people.sort(key=lambda x: (-x[0], x[1]))
        
        queue = []
        for person in people:
            # Insert each person at the index equal to their k-value
            queue.insert(person[1], person)
            
        return queue