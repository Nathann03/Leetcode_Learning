"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:

                ┌───┐
          ┌─────┤ 3 ├─────┐
          │     └───┘     │
        ┌─┴─┐           ┌─┴─┐
        ┤ 9 ├         ┌─┤20 ├─┐  
        └───┘         │ └───┘ │
                    ┌─┴─┐   ┌─┴─┐
                    │ 15│   │ 7 │
                    └───┘   └───┘

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2
"""

"""
Thought Process:

Magic:
Knowing that we will need to traverse down to each leaf to figure out
which is the deepest leaf, how can we do that while tracking the
depth it is currently at?

Lets use the magical method of Depth First Search (DFS)! DFS works thru
the tree from left to right where it goes to the left most path 
until it hits a leaf and then backtracks to most prev mode and takes
the right path and continues left until it needs to backtrack.

How does this help us? Well we will do the recursive (easiest) implementation
of DFS, which allows us to return the depth of either side and compare
using max() to choose the highest value of the two.

Recursive thought process:
Base Case - If node is none, return 0
Main case - recur call left and right node and find the max of the two
            then add 1 to account for current node when returning for
            upper node above it
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
