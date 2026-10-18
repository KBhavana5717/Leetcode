class Solution:
    def evaluate(self, expression: str) -> int:
        def parse(expression: str, context: dict) -> int:
            if expression[0] != '(':
                if expression.lstrip('-').isdigit():
                    return int(expression)
                return context[expression]
            
            # Remove outer parenthesis
            tokens = []
            bal = 0
            j = 1
            for i in range(1, len(expression) - 1):
                if expression[i] == '(':
                    bal += 1
                elif expression[i] == ')':
                    bal -= 1
                elif expression[i] == ' ' and bal == 0:
                    tokens.append(expression[j:i])
                    j = i + 1
            tokens.append(expression[j:len(expression) - 1])
            
            if tokens[0] == 'add':
                return parse(tokens[1], context) + parse(tokens[2], context)
            elif tokens[0] == 'mult':
                return parse(tokens[1], context) * parse(tokens[2], context)
            else: # let expression
                new_context = context.copy()
                for i in range(1, len(tokens) - 1, 2):
                    if i + 1 < len(tokens):
                        new_context[tokens[i]] = parse(tokens[i + 1], new_context)
                return parse(tokens[-1], new_context)

        return parse(expression, {})