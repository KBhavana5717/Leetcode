class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        res = []
        
        def backtrack(index: int, path: str, eval_val: int, mult_val: int):
            if index == len(num):
                if eval_val == target:
                    res.append(path)
                return
            
            for i in range(index, len(num)):
                # Numbers cannot have leading zeros
                if i != index and num[index] == '0':
                    break
                    
                curr_str = num[index:i+1]
                curr_val = int(curr_str)
                
                if index == 0:
                    backtrack(i + 1, curr_str, curr_val, curr_val)
                else:
                    backtrack(i + 1, path + "+" + curr_str, eval_val + curr_val, curr_val)
                    backtrack(i + 1, path + "-" + curr_str, eval_val - curr_val, -curr_val)
                    backtrack(i + 1, path + "*" + curr_str, eval_val - mult_val + mult_val * curr_val, mult_val * curr_val)
                    
        backtrack(0, "", 0, 0)
        return res