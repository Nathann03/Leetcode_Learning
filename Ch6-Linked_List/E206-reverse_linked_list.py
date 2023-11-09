"""
Given the head of a singly linked list, reverse the list, and return 
the reversed list.

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
"""

"""
Thought Process:

Naive/BF:
The Brute force way of doing this is iterating thru the entire list
and saving each node and then once done, just reconstructing it backwards.

Magic:
As this is a linked list problem, we should know that the best sol is 
usually an in-place solution to save time and space. So the idea here is
that we keep three pointers to use for flipping the next value as we 
always need to know what is before, current, and after since once we
change the current to prev, we wouldn't have a way to go next w/o that 
third ptr.

Crux of this problem:
The hardest part is figuring out which order the ptrs go since once small
mistake causes an out of bounds error woo. 
1st iter: prev = None
init curr = last head in cycle -> init next -> curr.next = prev 
-> prev = curr
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head is not None:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        
        return prev


