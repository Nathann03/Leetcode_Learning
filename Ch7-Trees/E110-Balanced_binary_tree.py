"""
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth 
of the two subtrees of every node never differs by more than one.


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
"""

"""
Thought process:

Magic:
As usual, the main part of this problem that we need to consider is 
the detail. The devil is always in the details.

Taking this at face value, we might just do a depth check on
the left and right subtree of the root to check if their depth is
within +/- 1 between each other, but if we read carefully, the subtrees
of the root also have to be height balanced. We could have a situation
where the left branch could be two less of the right branch in a subtree
which means the entire binary tree is not height balanced.

So how do we account for this. As usual using the power of recursion,
we can easily solve this problem. Similar to E543 - diameter of the tree
solution, we can kind of extrapolate the solution from the naive/false
conclusion before reading the details.

Seeing as we always need to check if the left and right subtree depth,
we can use recursion to make this problem be broken down to subtree
subproblems where we check every node starting from leaf is balanced
and if it deviates more than +/- 1, we can return a flag to returns
the solution without having to continually do the calculation.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height_bal(node):
            if node is None:
                return 0
            
            h_left = height_bal(node.left)
            h_right = height_bal(node.right)

            if h_left == -1 or h_right == -1 or abs(h_left - h_right) > 1:
                return -1
            
            return 1 + max(h_left, h_right)
        
        return height_bal(root) != -1