class Solution:
    def countOfAtoms(self, formula: str) -> str:
        from collections import defaultdict
        
        stack = [defaultdict(int)]
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                # Parse multiplier after ')'
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[i_start:i]) if i_start < i else 1
                
                top = stack.pop()
                for atom, count in top.items():
                    stack[-1][atom] += count * multiplier
            else:
                # Parse element name
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[i_start:i]
                
                # Parse element count
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[i_start:i]) if i_start < i else 1
                
                stack[-1][atom] += count
                
        # Sort and format the result
        final_map = stack[0]
        res = []
        for atom in sorted(final_map.keys()):
            res.append(atom)
            if final_map[atom] > 1:
                res.append(str(final_map[atom]))
                
        return "".join(res)