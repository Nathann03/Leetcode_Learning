"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

"""
Thought process:

Naive/BF:
Couldn't think of one

Magic:
The main idea of this is that if we have a set of parentheses, we can't
have any interlocking parentheses like "([)]". It has to be equivalent
to the last/most recent opening brace to close it out. Therefore, the
best solution to use is putting all of the opening braces in a stack and
when ever we encounter a closing brace, cross check it to see if it matches
the most recent opening brace, if not, failure.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}
        for par in s:
            if par in "({[":
                stack.append(par)
            else:
                if not stack or par != mapping.get(stack[-1]):
                    return False
                stack.pop()
        return not stack

