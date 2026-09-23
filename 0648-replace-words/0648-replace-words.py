class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        # Convert dictionary to a set for O(1) lookups
        root_set = set(dictionary)
        
        words = sentence.split()
        result = []
        
        for word in words:
            replacement = word
            # Check prefixes of increasing length
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in root_set:
                    replacement = prefix
                    break
            result.append(replacement)
            
        return " ".join(result)