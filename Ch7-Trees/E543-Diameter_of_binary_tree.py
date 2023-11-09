"""
Given the root of a binary tree, return the length of the diameter of 
the tree.

The diameter of a binary tree is the length of the longest path 
between any two nodes in a tree. This path may or may not pass 
through the root.

The length of a path between two nodes is represented by the number 
of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
"""

"""
Thought Process:

Magic:
Well this problem may seem very simple as it looks fairly similar to
the max depth question E104 that we did earlier where we can just
DFS the left subtree and right subtree to find the depth of both and
add them together to get the "diameter" of the tree.

However, the trick/deception is in the details (THE DEVILL)! Looking
at this, it only specifies that it is a binary tree, not a balanced
binary tree, so that means that we could have a subtree that has
really long branches and have a wider diameter from left to right
than our subtree if we dfs left and right. So how do we account for
this?

Well we can kind of iterate on this where for each subtree, we do
the above method of finding the depth of left and right and seeing if
it is the biggest diameter we have seen since technically all
subtrees will have its largest diameter be its left + right + 1,
we just need to store the max from all subtrees starting from the root.

But how do we store this global diameter variable that we can call 
during the recursion stack?

We use the power of "nonlocal" which allows nested functions to refer
to its parent function's variables, so when we call this nested func
recursively, it should always have access to its parent func variable
globally.

Recursive thinking:
Base case: If not a node, return 0
General case: call global var for current max diam seen, 
              call recursively depth of left and right subtree
              calculate diameter of subtree
              return the longest branch depth using max of left and right
              + 1 (+1 for current node btw)

Crux of the problem:
Recursive thinking can be pretty difficult especially when thinking 
of edge cases that we need to be aware of. Also, the idea that it is
not a balances binary tree can trip you up.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def depth(node) -> int:
            nonlocal max_diameter

            if node is None:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)

            max_diameter = max(max_diameter, left + right)

            return 1 + max(left, right)
        
        depth(root)
        return max_diameter

"""
Note if nonlocal kinda wierds you out, we can mess around with the solution
class to do an init that we can use to store the max diameter as a class
var which works the same way as shown below.
"""
class Solution:
    def __init__(self):
        self.diameter = 0  # stores the maximum diameter calculated
	
    def depth(self, node: Optional[TreeNode]) -> int:
        """
        This function needs to do the following:
            1. Calculate the maximum depth of the left and right sides of the given node
            2. Determine the diameter at the given node and check if its the maximum
        """
        # Calculate maximum depth
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0
        # Calculate diameter
        if left + right > self.diameter:
            self.diameter = left + right
        # Make sure the parent node(s) get the correct depth from this node
        return 1 + (left if left > right else right)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        self.depth(root)  # root is guaranteed to be a TreeNode object
        return self.diameter