"""
Given the head of a linked list, reverse the nodes of the list k at a 
time, and return the modified list.

k is a positive integer and is less than or equal to the length of the 
linked list. If the number of nodes is not a multiple of k then left-out 
nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves 
may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
"""

"""
Thought Process:

Naive:
The naive solution for reversing nodes in a linked list in groups of k 
operates iteratively by maintaining three pointers: prev_group_end, 
group_start, and group_end. It reverses nodes within a group of size k 
while keeping track of the last node of the previous group. This process 
is repeated until there are fewer than k nodes remaining to reverse. For 
each group, it reverses the next pointers of the nodes, connects the 
previous group to the reversed group, and continues to the next group. 

Magic:
Lets keep this idea of iteratively but instead of slicing and joining
idea lets use the power of a dummy node and runners (rabbit & tortoise).
If we remember the solution to M19-remove nth node, we modified rabbit
and tortoise so it is staggered race instead of a fast vs slow race.
We can apply this here where we stagger every k (given) in the linked
list and reverse the list between the tortoise and the hare. Once we 
are done with this, we reset the "start" of the race to where the hare
was and redo this stagger until we reach the end of the list and the
total number of node (keep track using var) is less than k.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1: return head
        dummy = next_head = ListNode(None)
        dummy.next = head
        prev = curr = head

        while True:
            count = 0
            while curr and count < k:
                count += 1
                curr = curr.next
            if count == k:
                h, t = curr, prev   # assign the first node of next k-group and the first node of current k-group to h(ead), t(ail)
                for _ in range(k):   # this is NOT a standard reversing by swapping arrows between adjacent nodes
                    tmp = t.next     # instead it poplefts a node successively and attaches it to next kgroup or most recently popped left node
                    t.next = h
                    h = t
                    t = tmp
                    # one-line implementation: t.next, t, h = h, t.next, t
                next_head.next = h   # connect the last node of the previous reversed k-group to the head of the current reversed k-group
                next_head = prev     # prepare for connecting to the next to-be-reversed k-group
                prev = curr   # head of the next yet to be reversed k-group
            else:   # curr = None and count does not reach k i.e. list is exhausted
                return dummy.next