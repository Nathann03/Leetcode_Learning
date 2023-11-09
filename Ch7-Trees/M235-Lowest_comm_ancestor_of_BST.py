"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) 
node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common 
ancestor is defined between two nodes p and q as the lowest node in 
T that has both p and q as descendants (where we allow a node to be 
a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
"""

"""
Thought Process:

Naive:
The Naive/Brute Force solution to this is to iteratively (not rec) to 
go through each node and find where the given nodes are and figure
out where they are relative to the root. We then just work our way
backwards until they reach a node that is the smallest node that has
them still as a descendant of them both.

Magic:
As usual for tree problems, lets think of this in terms of breaking it 
down in subproblems using subtrees.

So how do we know when the lowest common ancestor is and how does it
relate to the root?

In terms of the attributes of a BST, the left node is smaller and the
right node is bigger than the current node we are at. Following this,
all nodes to the left are smaller and all nodes to the right are bigger.
Since the nodes given have to be descendents of the LCA, we know that
if we have one bigger and one smaller node given than the root of x
subtree, we know that the only common ancestor is the current root.
Therefore, the answer is the root.

However, what if the largest node of the two is smaller than the root,
then we will need to traverse down left until we reach the condition of it
being between the values. Also, if the smallest value is bigger than the
root, we do the same thing except move the root right.

Recursive thinking:

Base case: small <= root <= large -> return root

Main thinking: max(node1, node2) < root -> return root.left
               min(node1, node2) > root -> return root.right


Now thinking about this, since this is just a normal search within a 
BST, why do we need to do this recursively? We can just move root itself
since we are just searching for a specific case that is guaranteed to be
in the tree.

Lesson Learned: For searches, no need for a recursive approach, just a
                binary search approach of narrowing down iteratively
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small = min(p.val, q.val)
        big = max(p.val, q.val)

        while root:
            if small > root.val:
                root = root.right
            elif big < root.val:
                root = root.left
            elif small <= root.val <= big:
                return root
        
        return None
        