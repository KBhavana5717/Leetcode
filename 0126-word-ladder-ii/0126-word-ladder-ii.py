from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
            
        # Distance dictionary to track the shortest path distance from beginWord
        distances = {beginWord: 0}
        # Adjacency list to record parents for backtracking
        parents = defaultdict(list)
        
        queue = deque([beginWord])
        found = False
        
        # Step 1: BFS to find the shortest paths and build parent relationships
        while queue and not found:
            visited_in_level = set()
            for _ in range(len(queue)):
                word = queue.popleft()
                current_distance = distances[word]
                
                if word == endWord:
                    found = True
                    continue
                
                # Generate all possible single-letter transformations
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        
                        if next_word in word_set:
                            if next_word not in distances:
                                distances[next_word] = current_distance + 1
                                visited_in_level.add(next_word)
                                queue.append(next_word)
                                parents[next_word].append(word)
                            elif distances[next_word] == current_distance + 1:
                                parents[next_word].append(word)
                                
            # Add words visited in this level to the main word set to prevent cycles across levels
            word_set -= visited_in_level
            
        # Step 2: Backtracking (DFS) to reconstruct all shortest paths
        result = []
        
        def backtrack(current_word: str, path: list[str]):
            if current_word == beginWord:
                result.append(path[::-1])
                return
            for p in parents[current_word]:
                path.append(p)
                backtrack(p, path)
                path.pop()
                
        if found:
            backtrack(endWord, [endWord])
            
        return result