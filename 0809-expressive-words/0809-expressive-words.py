class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        def get_rle(word):
            chars, counts = [], []
            i = 0
            while i < len(word):
                char = word[i]
                count = 0
                while i < len(word) and word[i] == char:
                    count += 1
                    i += 1
                chars.append(char)
                counts.append(count)
            return chars, counts

        s_chars, s_counts = get_rle(s)
        ans = 0

        for word in words:
            w_chars, w_counts = get_rle(word)
            if s_chars != w_chars:
                continue
            
            is_stretchy = True
            for sc, wc in zip(s_counts, w_counts):
                if wc > sc or (sc < 3 and wc != sc):
                    is_stretchy = False
                    break
            
            if is_stretchy:
                ans += 1

        return ans