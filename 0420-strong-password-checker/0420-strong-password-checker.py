class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        # Check missing types (lowercase, uppercase, digit)
        has_lower = any('a' <= c <= 'z' for c in password)
        has_upper = any('A' <= c <= 'Z' for c in password)
        has_digit = any('0' <= c <= '9' for c in password)
        missing_types = 3 - (has_lower + has_upper + has_digit)
        
        replaces = 0
        seqs = []
        
        # Find lengths of repeating sequences
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            if length >= 3:
                replaces += length // 3
                seqs.append(length)
            i = j
            
        # Case 1: Password is too short (n < 6)
        if n < 6:
            return max(6 - n, missing_types)
        
        # Case 2: Password length is within the valid range (6 <= n <= 20)
        elif n <= 20:
            return max(replaces, missing_types)
        
        # Case 3: Password is too long (n > 20)
        else:
            deletions = n - 20
            deletions_left = deletions
            
            # 1. Prioritize sequences where length % 3 == 0 (cost = 1 deletion)
            new_seqs = []
            for length in seqs:
                if length % 3 == 0 and deletions_left >= 1 and replaces > 0:
                    deletions_left -= 1
                    replaces -= 1
                    length -= 1
                if length >= 3:
                    new_seqs.append(length)
            seqs = new_seqs
            
            # 2. Prioritize sequences where length % 3 == 1 (cost = 2 deletions)
            new_seqs = []
            for length in seqs:
                while length >= 4 and length % 3 == 1 and deletions_left >= 2 and replaces > 0:
                    deletions_left -= 2
                    replaces -= 1
                    length -= 2
                if length >= 3:
                    new_seqs.append(length)
            seqs = new_seqs
            
            # 3. Prioritize sequences where length % 3 == 2 (cost = 3 deletions)
            new_seqs = []
            for length in seqs:
                while length >= 5 and length % 3 == 2 and deletions_left >= 3 and replaces > 0:
                    deletions_left -= 3
                    replaces -= 1
                    length -= 3
                if length >= 3:
                    new_seqs.append(length)
            seqs = new_seqs
            
            # Use any remaining deletions on any remaining sequences (cost = 3 deletions)
            for length in seqs:
                while deletions_left >= 3 and replaces > 0:
                    deletions_left -= 3
                    replaces -= 1
                    
            return deletions + max(replaces, missing_types)