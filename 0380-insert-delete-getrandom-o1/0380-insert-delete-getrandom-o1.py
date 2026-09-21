import random

class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
            
        # Get the index of the element to remove
        idx = self.val_to_index[val]
        last_val = self.values[-1]
        
        # Move the last element to the place of the element to be deleted
        self.values[idx] = last_val
        self.val_to_index[last_val] = idx
        
        # Remove the target element
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)