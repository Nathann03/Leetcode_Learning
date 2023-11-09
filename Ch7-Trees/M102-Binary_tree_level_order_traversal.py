"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:

                ┌───┐
          ┌─────┤ 3 ├─────┐            Level 0 : [3]
          │     └───┘     │
        ┌─┴─┐           ┌─┴─┐
        ┤ 9 ├         ┌─┤20 ├─┐        Level 1 : [9, 20]
        └───┘         │ └───┘ │
                    ┌─┴─┐   ┌─┴─┐
                    │ 15│   │ 7 │      Level 2 : [15, 7]
                    └───┘   └───┘

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []
"""

"""
Thought Process:

Naive:
Th Naive/BF approach would be iterating through the tree nodes in a 
systematic manner starting at the root node, processing all 
nodes at the current level before moving on to the next level. You'd 
need to maintain some data structures to keep track of the current 
level's nodes and the nodes of the next level. In each level, you'd 
append the values of the nodes to a result list in the order they are 
encountered. This brute-force method would involve nested loops and 
require careful management of data structures to ensure the proper 
order of traversal. The time complexity of this brute-force approach 
would typically be O(n^2)

Magic (DFS - The initial idea/intuition):
The initial idea behind this is since we need to be moving from left
to right for each level to get a level order traversal, we know DFS
moves to the left most branches before moving over, so this would be
an obvious solution.

The crux of this problem is how do we save the node's value and put
it into a list that we will return later? Well, since DFS is recursive,
we can use the power of nonlocal to call for vars outside of the scope of
the recursive child function.


Magic pt.2 (BFS - Thought of last):
Seeing part 1 and its solution, clearly it is a very good solution, but
there is only one issue. It is very memory intensive as we are going to
each node and adding a whole frame that contains the non-local level_order
in the stack frame which takes up unnecessary space.

How do we avoid this use of space, well lets look at DFS' counter part
Breadth-first search(BFS). The idea of BFS is that it pretty much does
level-order traversal in its function where we want to visit each level
first before we head on deeper (Kinda like in a video game where you
don't want to fight a boss yet because you are pot missing out on loot).
The best part about BFS is that it is done iteratively, so we do not
need to rely on the stack for everything, saving space in memory.

How does BFS achieve this?
The key to BFS's level-order traversal lies in its use of a queue, 
a first-in-first-out (FIFO) data structure. When starting from the root
node, BFS enqueues the initial node, then iteratively dequeues nodes 
from the front of the queue and enqueues their child nodes in the order 
they were encountered (Left to right). This process continues until 
the queue is empty, effectively ensuring that nodes at the same level 
are processed before nodes at deeper levels. By maintaining this FIFO 
order, BFS guarantees that it explores all nodes at the current level 
before moving to the next.

By using BFS, we can achieve both 
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS Solution
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = []

        def dfs(node, level):
            nonlocal level_order
            
            if node is None:
                return
            
            if level > (len(level_order) - 1):
                level_order.append([])
            
            level_order[level].append(node.val)
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        dfs(root)
        return level_order

# BFS Solution
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        # Sanity Check
        if root is None: 
            return root
        
        res = []
        
        # keep track of nodes in each level from left to right
        queue = [] 
        # first node (root) is added to queue which we'll be later 
        # added to level and then finally res
        queue.append(root) 
        
        # we keep going until there is something in queue. Empty queue 
        # means we have covered every node
        while len(queue) > 0: 
            level = [] # This collects every node is each level. Note the output format in the problem statement. Nodes of each level are a sublist within the final output list res
            for i in range(len(queue)): # it goes over length of queue which includes all the elements of current level, and each of them is added to the level variable. 
                node = queue.pop(0) # removes the first element of the list. In contrast to pop() that removes last element and is used for stack data structure. Note that first element is added 
                level.append(node.val) # append the value of current node
            
                if node.left != None: # queue gets updated by adding left child. The traversal occurs from left to right
                    queue.append(node.left)
                if node.right != None: # queue gets updated by adding right child. 
                    queue.append(node.right)
            res.append(level) # we're done with this level, and we append level to the res variable
        return res
            