class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.",
            "....","..",".---","-.-",".-..","--","-.",
            "---",".--.","--.-",".-.","...","-","..-",
            "...-",".--","-..-","-.--","--.."
        ]
        transformations = {"".join(morse[ord(c) - ord('a')] for c in word) for word in words}
        return len(transformations)