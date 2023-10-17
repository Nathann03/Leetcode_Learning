"""
You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order, and each of their nodes 
contains a single digit. Add the two numbers and return the sum as a 
linked list.

You may assume the two numbers do not contain any leading zero, except 
the number 0 itself.

Important to know: The numbers are listed in reverse!!!

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

"""
Thought Process:

Naive:
The Naive way of doing this is doing one pass through, storing the value
of both linked lists, reversing them, then adding the numbers together.
Afterwards, we just make a linked list of each digit from small to large.

Magic:
Well Watson, this is merely elementary, well elementary math to solve this
problem. Seeing as this problem is just doing math the common core way
where we just iterate through the list and add the numbers. If the 
numbers are greater than 10, we just do some mod to get the remainer and 
subtraction (by 10) to get the value we need to add to the new LL node digit.

Crux of this problem: PLEASE READ THE EXAMPLES MY GUY GOD DAMN IT. While
it does say that the nimber does not have any leading zeros, that doesn't
mean that it will be two numbers of the same length (as shown on ex 3).
So we will have to account for that ugh

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode(0)
        carry = 0

        while l1 is not None or l2 is not None:
            num1, num2 = 0, 0

            if l1 is not None:
                num1, l1 = l1.val, l1.next
            
            if l2 is not None:
                num2, l2 = l2.val, l2.next
            
            summation = num1 + num2 + carry
            curr.next = ListNode(summation % 10)

            curr = curr.next
            carry = summation // 10
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return head.next



