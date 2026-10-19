import re
from collections import defaultdict
from typing import List

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        env = dict(zip(evalvars, evalints))
        tokens = re.findall(r'[a-z]+|\d+|[()+\-*]', expression)
        pos = 0

        # polynomial = dict: tuple of sorted variable names -> coefficient
        def add(p1, p2, sign=1):
            res = defaultdict(int)
            for k, v in p1.items():
                res[k] += v
            for k, v in p2.items():
                res[k] += sign * v
            return {k: v for k, v in res.items() if v != 0}

        def mul(p1, p2):
            res = defaultdict(int)
            for k1, v1 in p1.items():
                for k2, v2 in p2.items():
                    res[tuple(sorted(k1 + k2))] += v1 * v2
            return {k: v for k, v in res.items() if v != 0}

        # expr := term (('+' | '-') term)*
        def parse_expr():
            nonlocal pos
            result = parse_term()
            while pos < len(tokens) and tokens[pos] in '+-':
                op = tokens[pos]
                pos += 1
                right = parse_term()
                result = add(result, right, 1 if op == '+' else -1)
            return result

        # term := factor ('*' factor)*
        def parse_term():
            nonlocal pos
            result = parse_factor()
            while pos < len(tokens) and tokens[pos] == '*':
                pos += 1
                result = mul(result, parse_factor())
            return result

        # factor := '(' expr ')' | number | variable
        def parse_factor():
            nonlocal pos
            tok = tokens[pos]
            pos += 1
            if tok == '(':
                result = parse_expr()
                pos += 1  # skip ')'
                return result
            if tok.isdigit():
                n = int(tok)
                return {(): n} if n != 0 else {}
            if tok in env:
                v = env[tok]
                return {(): v} if v != 0 else {}
            return {(tok,): 1}

        poly = parse_expr()

        # sort: higher degree first, then lexicographic by variables
        keys = sorted(poly.keys(), key=lambda k: (-len(k), k))
        ans = []
        for k in keys:
            if k:
                ans.append(str(poly[k]) + '*' + '*'.join(k))
            else:
                ans.append(str(poly[k]))
        return ans