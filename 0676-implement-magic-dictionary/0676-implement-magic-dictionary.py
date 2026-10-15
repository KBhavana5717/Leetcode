class MagicDictionary:

    def __init__(self):
        self.words = set()
        self.neighbors = collections.defaultdict(set)

    def buildDict(self, dictionary: list[str]) -> None:
        self.words = set(dictionary)
        for word in dictionary:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                self.neighbors[pattern].add(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            pattern = searchWord[:i] + '*' + searchWord[i+1:]
            if pattern in self.neighbors:
                for word in self.neighbors[pattern]:
                    if word != searchWord:
                        return True
        return False