"""
Given the root of a binary tree, imagine yourself standing on the 
right side of it, return the values of the nodes you can see ordered 
from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

"""
Thought Process:

Naive/BF:
Honestly, for Tree problems, there isn't really any Naive/BF solutions
that you can choose since most of them are bfs/dfs, so no reason to waste
time to do it

Magic:
Looking at this question, the hardest part of this question really is
understand what it is asking imo. To make it more readable, the question
is asking that if you were standing to the right of the tree and looking
at it, what nodes would you see from top to bottom (i.e. the right most
node of every level).

Seeing that this is a level problem, we know that this question is similar
to M102 for level order traversal. However, the crux of this problem is
that traditional level order traversal, BFS & DFS, they generally work
from left to right so how do we work from right to left this time?

Well two solutions come to mind to either avoid or tackle this crux.

To tackle the issue (The better solution):
Knowing how DFS works, we generally regard it as going from left to right
when traversing a tree, but why is that? That is because we call the
recursive func for the left node before the right node, so what if we
reverse it. Therefore, we get the outcome we want of going right to left.

Now knowing this, we can use the same DFS solution as M102 where we keep
a nonlocal list and store the first instance of the node value when we 
see of a new level. The level is tracked by a list, so we just check len
list for lowest level we have seen before.

To avoid the issue:
Since technically we are moving left to right in DFS, the last value we
encounter of a specific level will be the right most value, so we just
keep changing the value of the result list idx corresponding to level and
the result after going thru all nodes will be all the right most nodes.
This solution takes up a very small amount of real time (not O time), so
in theory this is worse.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS Solution
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        
        def dfs(node, level):
            if node is None:
                return
            
            if len(self.res) == level:
                self.res.append(node.val)
            
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return self.res

# BFS Solution (Not mine)
class Solution:
    def rightSideView(self, root):
        deque = collections.deque()
        if root:
            deque.append(root)
        res = []
        while deque:
            size, val = len(deque), 0
            
            for _ in range(size):
                node = deque.popleft()
                val = node.val # store last value in each level
                
                if node.left is not None:
                    deque.append(node.left)
                if node.right is not None:
                    deque.append(node.right)
            
            res.append(val)
        return res
        

