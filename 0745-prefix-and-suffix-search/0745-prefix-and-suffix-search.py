class WordFilter:

    def __init__(self, words: list[str]):
        self.memo = {}
        for idx, word in enumerate(words):
            length = len(word)
            for i in range(min(length, 7) + 1):
                pref = word[:i]
                for j in range(min(length, 7) + 1):
                    suff = word[length - j:]
                    self.memo[(pref, suff)] = idx

    def f(self, pref: str, suff: str) -> int:
        return self.memo.get((pref, suff), -1)