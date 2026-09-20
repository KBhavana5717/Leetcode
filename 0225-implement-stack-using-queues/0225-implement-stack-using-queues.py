class MyStack:

    def __init__(self):
        self.q=[]
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.push(self.q.pop(0))
        return self.q.pop(0)            

    def top(self) -> int:
        top_element=self.pop()
        self.push(top_element)
        return top_element

    def empty(self) -> bool:
        return not self.q
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()