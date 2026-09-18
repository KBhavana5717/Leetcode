class Solution(object):
    def reverseWords(self, s):
        stack=[]
        t=s.strip().split()
        r=[]
        for i in t:
            stack.append(i)
        while stack:
            r.append(stack.pop()) 
        return " ".join(r)    