class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            # swapping two equal letters keeps the string the same
            return len(set(s)) < len(s)

        diff = [i for i in range(len(s)) if s[i] != goal[i]]

        return (
            len(diff) == 2
            and s[diff[0]] == goal[diff[1]]
            and s[diff[1]] == goal[diff[0]]
        )