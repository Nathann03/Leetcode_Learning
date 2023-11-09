"""
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:
                ┌───┐
          ┌─────┤ 4 ├─────┐
          │     └───┘     │
        ┌─┴─┐           ┌─┴─┐
      ┌─┤ 2 ├─┐       ┌─┤ 7 ├─┐  
      │ └───┘ │       │ └───┘ │
    ┌─┴─┐   ┌─┴─┐   ┌─┴─┐   ┌─┴─┐
    │ 1 │   │ 3 │   │ 6 │   │ 9 │
    └───┘   └───┘   └───┘   └───┘

                INTO
                ┌───┐
          ┌─────┤ 4 ├─────┐
          │     └───┘     │
        ┌─┴─┐           ┌─┴─┐
      ┌─┤ 7 ├─┐       ┌─┤ 2 ├─┐
      │ └───┘ │       │ └───┘ │
    ┌─┴─┐   ┌─┴─┐   ┌─┴─┐   ┌─┴─┐
    │ 9 │   │ 6 │   │ 3 │   │ 1 │
    └───┘   └───┘   └───┘   └───┘ 

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
"""

"""
Thought Process:
By executive decision (lmao me only), I have decided that most 
easy questions won't have any naive solution provided since these are 
the building blocks needed for all the questions involving this data type

Magic:
So how would we invert a binary tree to its core since the tree looks
like it was put thru a mirror. For example 1, we can see even the left
leaves of the tree get swapped to the right (1 - 3 to 3 - 1).

Revolutionary idea: Lets break this down into subtree problems and
combine it with the power of recursion, which is pretty effective against
tree problems.

Recursion Problem solving:
Base case: If sub-tree is a leaf, just return the leaf
Main: Calling the left and right subtree of the current node and then
      swapping the left and right nodes to be the opposite side

With this solution, we can easily solve the problem!
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root