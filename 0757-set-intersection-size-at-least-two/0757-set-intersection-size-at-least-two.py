class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        todo = [2] * len(intervals)
        ans = 0
        
        while intervals:
            s, e = intervals.pop()
            t = todo.pop()
            
            for p in range(s, s + t):
                for i in range(len(intervals)):
                    if todo[i] > 0 and p <= intervals[i][1]:
                        todo[i] -= 1
                ans += 1
                
        return ans