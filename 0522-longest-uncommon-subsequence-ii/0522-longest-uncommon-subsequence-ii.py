class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        def is_subsequence(s1: str, s2: str) -> bool:
            # Check if s1 is a subsequence of s2
            it = iter(s2)
            return all(c in it for c in s1)

        # Sort strings by length in descending order
        strs.sort(key=len, reverse=True)
        
        # Check each string against all other strings
        for i, s1 in enumerate(strs):
            found = True
            for j, s2 in enumerate(strs):
                if i == j:
                    continue
                if is_subsequence(s1, s2):
                    found = False
                    break
            if found:
                return len(s1)
                
        return -1