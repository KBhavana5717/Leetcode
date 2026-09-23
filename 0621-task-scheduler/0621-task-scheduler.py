from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Count the frequency of each task
        count = Counter(tasks)
        
        # Find the maximum frequency of any task
        max_freq = max(count.values())
        
        # Count how many tasks share this maximum frequency
        max_count = sum(1 for freq in count.values() if freq == max_freq)
        
        # Calculate the minimum intervals based on the most frequent task
        part_count = max_freq - 1
        part_length = n + 1
        empty_slots = part_count * part_length + max_count
        
        # The answer is either the calculated empty slots or the total number of tasks
        return max(empty_slots, len(tasks))