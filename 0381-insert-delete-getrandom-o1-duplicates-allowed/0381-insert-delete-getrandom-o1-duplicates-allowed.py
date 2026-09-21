import random

class RandomizedCollection:

    def __init__(self):
        self.list = []
        self.map = {}

    def insert(self, val: int) -> bool:
        # Check if the value already exists in the map
        is_not_present = val not in self.map
        
        if is_not_present:
            self.map[val] = set()
            
        # Add the index of the new element to its set of indices
        self.map[val].add(len(self.list))
        self.list.append(val)
        
        return is_not_present

    def remove(self, val: int) -> bool:
        if val not in self.map or not self.map[val]:
            return False
        
        # Get an arbitrary index of the value to remove
        remove_index = self.map[val].pop()
        last_element = self.list[-1]
        
        # If the element to remove is not the last one, swap it with the last element
        if remove_index < len(self.list) - 1:
            self.list[remove_index] = last_element
            # Update the index of the last element in the map
            self.map[last_element].add(remove_index)
            self.map[last_element].remove(len(self.list) - 1)
            
        # Remove the last element from the list
        self.list.pop()
        
        # Clean up the dictionary entry if the set of indices becomes empty
        if not self.map[val]:
            del self.map[val]
            
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)