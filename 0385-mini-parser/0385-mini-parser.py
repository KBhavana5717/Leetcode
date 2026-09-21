class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        self.i = 0
        
        def helper() -> NestedInteger:
            # If it's a single integer (does not start with '[')
            if s[self.i] != '[':
                start = self.i
                while self.i < len(s) and (s[self.i].isdigit() or s[self.i] == '-'):
                    self.i += 1
                return NestedInteger(int(s[start:self.i]))
            
            # Otherwise, it's a list starting with '['
            res = NestedInteger()
            self.i += 1 # skip '['
            
            while self.i < len(s) and s[self.i] != ']':
                if s[self.i] == ',':
                    self.i += 1 # skip comma separator
                    continue
                res.add(helper())
                
            self.i += 1 # skip ']'
            return res

        return helper()