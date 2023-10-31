"""
Given the roots of two binary trees p and q, write a function to 
check if they are the same or not.

Two binary trees are considered the same if they are structurally 
identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 
"""

"""
Thought Process:

Magic:
While it would be great if we were just given the post order list traversal
for the tree, we sadly only have the node for the root of the tree, so
how can we check if the trees given are identical?

The main intuition here is that we can traverse thru the tree similarly
for both trees and check if they are identical or not. However, the
structure may not be the same as shown in example two where p only has
a node attached to node.left while q only has a node attached to node.right.

The main crux of this problem is how do we differentiate between the two.

By the power of dfs, we can approach this problem from the bottom up. 
Since if we move onto a node after we traverse it and realize that one
is null while the other is a value or they are two different values,
we will know that they are different.

Therefore, we can break this problem down in terms of subtrees where we
check the current value of the node we are at since we are traversing
similarly and just do a simple value check between the two and if we
return false, with the use of AND for traversing left and right subtrees
we will send the false all the way back up to to the top for the solution.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False