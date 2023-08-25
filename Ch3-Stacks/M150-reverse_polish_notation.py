"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

"""

"""
Thought process:
I mean wtf, no like wtf is this question?!?! So the crux of this problem
is finding out what the fuck it is asking and how to evaluate it.

Naive/BF:
I dunno give up?

Magic:
So the main idea of this is that when we encounter an operation, we need
to combine the last/most recent 2 numbers/(results of other operations),
so we will need a DS that can do FIFO, so a STACKKKKK!

"""
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    result = num2 + num1
                elif token == "-":
                    result = num2 - num1
                elif token == "*":
                    result = num2 * num1
                else:
                    result = math.trunc(num2 / num1)

                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[0]