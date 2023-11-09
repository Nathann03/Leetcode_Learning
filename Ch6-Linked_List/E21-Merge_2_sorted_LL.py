"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""

"""
Thought Process:

Naive:
The brute force solution to this is saving all the nodes and ordering them
after sorting them. To sort them, we just have 2 connected consecutive 
lists and do a bubble sort on the list with just the values and move 
the associated node in the other list to the correct spot.

Magic:
As we know, for linked lists, in place is kingggg! Since the LL are 
already in order, why not just use two ptr and compare each node. The
smallest node of the two gets added to a new LL until all nodes are
exhausted.

The crux of this problem is establishing a new linked list. We can use
the amazing trick of creating a dummy node! By creating a dummy node at the
beginning, we don't have to create an exception for initial run. We just
have to return dummy_node.next!
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode(0)

        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                curr.next = list2
                curr = list2
                list2 = list2.next
            else:
                curr.next = list1
                curr = list1
                list1 = list1.next
        
        if list1 is None:
            curr.next = list2
        else:
            curr.next = list1

        return head.next