"""
You are given the head of a singly linked-list. The list can be 
represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves 
may be changed.


Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""

"""
Thought Process:

Naive:
The obvious Naive method is to store each node in a lsit and reorder the 
list using the form given.

Lets take a look at the form. It seems like every odd iter is just an
increasing of the first half of the values. Every even value is 
just the second half of the LL, but just reversed or going mono down. 


Magic:
As I always say, in place is key with linked lists, so how would we achieve
this form inplace. Actually it is pretty easy. If we could just find the
middle of the LL and split it in half, we can then just reverse the second
half of the for all the even iter values for the form.

Crux of the problem: How do we find the middle? Well we can use the amazing
tortoise and the hare algo where we use a slow and fast pointer where slow
goes +1 while fast goes +2. By the time fast hits the end, the slow ptr
must be in the middle!

After finding the middle and reversing the second half, we now have an
easy merging problem where we just alternate which one to add to the list.
Dummy node comes in again since we are merging woo!

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Finding middle
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        #reversing Middle

        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt    
        slow.next = None
        
        first_half, second_half = head, prev

        # Merging
        while second_half:
            next_node = first_half.next
            first_half.next = second_half
            first_half = second_half
            second_half = next_node
        
