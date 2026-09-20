# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Initialize stack with elements in reverse order for LIFO processing
        self.stack = list(reversed(nestedList))
    
    def next(self) -> int:
        # Ensures the next element is an integer, then pops it
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        # Unpack nested lists until we find an integer or empty the stack
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            # If it's a list, pop it and push its contents in reverse order
            self.stack.pop()
            self.stack.extend(reversed(top.getList()))
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())