class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        def is_subsequence(word: str, target: str) -> bool:
            it = iter(target)
            return all(c in it for c in word)

        longest_word = ""

        for word in dictionary:
            if is_subsequence(word, s):
                # Compare lengths, or if lengths are equal, pick the lexicographically smaller word
                if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                    longest_word = word

        return longest_word