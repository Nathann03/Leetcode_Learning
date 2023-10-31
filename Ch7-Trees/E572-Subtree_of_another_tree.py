"""
Given the roots of two binary trees root and subRoot, return true if 
there is a subtree of root with the same structure and node values of 
subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in 
tree and all of this node's descendants. The tree tree could also be 
considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
"""

"""
Thought Process:

Magic:
Looking at this question, it looks very similar to E100 - Same tree as
we will need to check if the given tree has a subtree that is similar
to tree 2.

The easy obvious intuition for this solution is iterating through each
node and finding a node that has the same value as the second tree's root
and if it is, we execute the same_tree.py solution to check if the tree
is the same. If not, we just keep iterating thru the first tree until
we encounter the same thing or run out of nodes.

How will we do this though?

Since we need to use DFS twice, once for the checking if the node
in tree one is equal to root of tree two and another for checking if the
trees are identical. Therefore, we can use the recursive method for both
and constantly check if they are similar when we see the node values match.
If they don't match, just recursive next node and same tree next.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if p is None and q is None:
                return True
            
            if p is None or q is None:
                return False
            
            if p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            
            return False
        
        if root is None:
            return False
        
        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        
