class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        i = 0
        n = len(words)
        
        while i < n:
            # Step 1: Find all words that can fit in the current line
            line_words = [words[i]]
            line_length = len(words[i])
            i += 1
            
            while i < n and line_length + 1 + len(words[i]) <= maxWidth:
                line_length += 1 + len(words[i])
                line_words.append(words[i])
                i += 1
                
            # Step 2: Format the line
            # If it's the last line or the line has only one word, left-justify it
            if i == n or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                res.append(line)
            else:
                # Fully justify the line
                total_chars = sum(len(w) for w in line_words)
                total_spaces = maxWidth - total_chars
                num_gaps = len(line_words) - 1
                
                spaces_per_gap = total_spaces // num_gaps
                extra_spaces = total_spaces % num_gaps
                
                line = ""
                for j in range(num_gaps):
                    line += line_words[j]
                    # Assign an extra space to the leftmost gaps if remainder exists
                    current_spaces = spaces_per_gap + (1 if j < extra_spaces else 0)
                    line += " " * current_spaces
                line += line_words[-1]  # Append the last word
                res.append(line)
                
        return res