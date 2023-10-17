"""
A linked list of length n is given such that each node contains an 
additional random pointer, which could point to any node in the list, 
or null.

Construct a deep copy of the list. The deep copy should consist of 
exactly n brand new nodes, where each new node has its value set to 
the value of its corresponding original node. Both the next and random 
pointer of the new nodes should point to new nodes in the copied list 
such that the pointers in the original list and copied list represent 
the same list state. None of the pointers in the new list should point 
to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where 
X.random --> Y, then for the corresponding two nodes x and y in the 
copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random
pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""

"""
Thought Process:

Naive/BF:
The immediate Brute force solution that jumps out to me is forgetting
about the deep copy part for the random pointer and just making a 
regular deep copy of the LL with val and next. Then passing through it
again to add each random pointer and try to find its counterpart by
going thru the old LL and checking what index it is at so we know where 
we need to point it in case of duplicates. This could take up to O(n^2)
time however.

Magic:
So what if we keep this idea of creating the list during a first pass
through, but only create the node and the value assoc w/ it. But the
question is what do we do with these nodes and what if there are nodes
with duplicate values, how do we know which node is which?

Here is a game changer: what if we just hash the entire node? that way
we can store each node in a dict and call it based on the old node 
from the given linked list.

Afterwards, during our second pass through we can fill in the rest of the
nodes since we can just hash out what node we need through calling it
in the dict using old_LL.next and old_ll.random. Once we pass thru it
again, we just return the hash of the head of the old LL.
With these 2 passes, it ends up being a runtime of O(2n)

Magic 2.0:
Lets keep iterating on this idea, how can we make this a one pass solution?
If we keep this storage idea and make it usable for one pass. What if 
we make the node with everything this time and if we don't see a 
certain node exists yet in the hash, we can just create it for use
later. Therefore, by the time we pass through all nodes, they should
all be set up correctly based on the hash
"""
from collections import defaultdict
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        curr = head

        while curr is not None:
            curr_node = Node(curr.val)
            nodes[curr] = curr_node
            curr = curr.next
        
        return_val = head

        while head is not None:
            nodes[head].next = nodes.get(head.next)
            nodes[head].random = nodes.get(head.random)
            head = head.next
        
        return nodes[return_val]