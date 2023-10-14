"""
Given the head of a linked list, remove the nth node from the end of the 
list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

"""
Thought process:

Naive:
The naive solution to this is to store every ptr to the every node in
a list and just index the latest pointer, which would be O(n) time.
However, that would be 2m space where m is the size of the LL, so
not worth it space wise

Magic:
As always, we need to find the inplace solution to this problem. If we 
think back to some techniques for linked list, one that stands out is
tortoise and the hare method using two slow and fast pointers to find
the middle. Doesn't this seem familiar, finding something is the goal, so
how can we modify this?

The main idea of this problem is using two pointers where one starts the
race and the other is staggered behind by n, so by the time the hare
reaches the end, the tortoise is where we want it to be!

The crux of the problem:
Well actually I can kinda take this back a little, we can't have the 
tortoise to be exactly on the node we are trying to get rid of. We want
it before so we can skip over it and remove the next node (aka the node
we want to get rid of)

Also, how do we get the stagger to start off? W

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        for _ in range(n):
            fast = fast.next

        # Potential missed error here. Sometimes n = len(LL) at n = 1, so 
        # the next value would be a Null val, so it is imperative to realize
        # that it will throw an error there.
        if fast is None:
            return head.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return headd