class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Dictionary to store the length of the path at each depth level
        path_len = {-1: 0}
        max_len = 0
        
        # Split input by newline to process line by line
        for line in input.split('\n'):
            # Determine the depth by counting the number of '\t' characters
            depth = line.count('\t')
            # Extract the actual name of the file or directory by stripping tabs
            name = line.lstrip('\t')
            
            # The length of the path at current depth is:
            # (length of parent path) + (length of current name) + (1 for the '/' separator)
            path_len[depth] = path_len[depth - 1] + len(name) + 1
            
            # If it's a file (contains a '.'), check if it's the longest absolute path
            if '.' in name:
                # Subtract 1 because we don't need a trailing slash for a file
                max_len = max(max_len, path_len[depth] - 1)
                
        return max_len