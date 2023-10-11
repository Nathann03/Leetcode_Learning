"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

IMPORTANTO:
You must implement a solution with O(1) time complexity for 
each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

"""
Thought process:

Naive/BF: 
There is not one, design problem not question prob

Magic:
So the main issue with this problem is that we need to do each function
in O(1) bc why not, but for example, get min if we only used a list would
be O(n). The crux of the problem is popping, if we pop an object we still
need to track what is the minimum and top without any issues.

The main idea here is using two stacks. One stack that holds all of the
values so we use it for all func except min and another stack that just
holds the minimum values for each action we have done. If we want to undo
(aka pop), we just take out the top from both and undo any action that
has been done.

"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]