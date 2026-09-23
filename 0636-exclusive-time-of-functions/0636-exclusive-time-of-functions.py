class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            fn_id, action, timestamp = log.split(':')
            fn_id, timestamp = int(fn_id), int(timestamp)
            
            if action == 'start':
                if stack:
                    # Add the elapsed time to the function currently at the top of the stack
                    res[stack[-1]] += timestamp - prev_time
                stack.append(fn_id)
                prev_time = timestamp
            else:
                # Pop the finished function and add the execution time including the end timestamp unit
                res[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
                
        return res