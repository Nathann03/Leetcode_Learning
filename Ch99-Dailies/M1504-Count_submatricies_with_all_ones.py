"""
Problem:
Given an m x n binary matrix `mat`, return the number of submatrices that have all ones.

Example 1:
Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation: 
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 13.

Example 2:
Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation: 
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 24.

Thought process:

Naive / Brute Force:
- Treat each cell as the bottom-right corner of a rectangle.
- Expand leftwards and upwards, keeping track of the minimum height.
- For each leftward expansion, add the minimum height to the result.
- Runtime: O(m^2 * n) — for each row, we scan left for each column and compute rectangles.
- Intuitive, easy to implement, but slow for large matrices.

Optimized O(m * n) Solution:
- Treat each row as a histogram, where height[j] = consecutive ones ending at that row.
- For each column j, compute:
    - left[j]  = number of consecutive columns to the left (including j) where height >= current
    - right[j] = number of consecutive columns to the right (including j) where height > current
- Contribution of column j = height[j] * left[j] * right[j]
  → counts all rectangles for which this column is the bottom row and includes this column.

Why left uses >= and right uses >:
- Left pass merges equal-height bars to extend the left span.
- Right pass uses strictly greater (>) to avoid double-counting rectangles
  that are already counted by the current column as the leftmost column.

Why we use a stack:
- The stack maintains a **monotonic increasing sequence of bars** as we scan the histogram.
- This lets us efficiently compute how far each bar can extend left or right without scanning all previous bars.
- When a bar is popped from the stack, its count represents **how many columns it can span**.
- By adding the popped bar’s count to the current bar, we “merge the span” of taller/equal bars
  to calculate the number of rectangles ending at this column correctly.
- Each bar is pushed and popped at most once, keeping the runtime O(n) per row.

Intuition:
- Brute force checks all possible rectangles ending at each pivot.
- Optimized solution precomputes how far each column can extend left and right using stacks.
- Multiplying left, right, and height gives the total number of rectangles efficiently.
- Mirrors the trapping rainwater problem's optimization: instead of scanning everything repeatedly,
  we precompute bounds (left/right max heights or spans) to get a linear-time solution.
"""


# O(m^2 * n) solution, way more intuitive
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        curr = [0] * c
        res = 0

        # iter through all roes
        for i in range(r):
            # First generate the current height of the row assuming this row is base, where we build on what happened in prev row
            for j in range(c):
                # If 1, add to current count of height at that column
                if mat[i][j] == 1:
                    curr[j] += 1
                # If 0, then the height is reset since we cannot make a rect 
                else:
                    curr[j] = 0
            
            # With these heights, move left to right for height column to count amt of rect that bottom right pivot can make where [i][j] is bottom right of rect
            for j in range(c):
                mini = curr[j]
                k = j
                
                # Move left from pivot to check if we can make bigger rect 
                while k >= 0 and mini != 0:
                    mini = min(mini, curr[k])
                    res += mini
                    k -= 1
        
        return res
            

# O(m * n) solution, not intuitive at all
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        curr = [0] * c
        res = 0

        # iter through all roes
        for i in range(r):
            # First generate the current height of the row assuming this row is base building on what happened in prev row
            for j in range(c):
                # If 1, add to current count of height at that column
                if mat[i][j] == 1:
                    curr[j] += 1
                # If 0, then the height is reset since we cannot make a rect 
                else:
                    curr[j] = 0
            
            stack = [] # Stack hold 
            left = [0] * c # num valid start points including self
            right = [0] * c

            # Find num valid starting points of rectangle to left of pivot inclusive of pivot
            # Move from left to right in histogram to see how far left each point can cover to see its
            # terminal smaller value point
            # We use >= here because bars of equal height can be merged into the span to the left.
            for j in range(c):
                count = 1
                
                # If current number is less than top of stack, we need to pop all numbers
                # bigger in the stack and add up their counts since if that big number can
                # cover left, then the smaller number can also cover left in the same amount + itself
                # ex [3, 2, 1] when at 1, all valid starting points would be itself and all left of it
                # stack from 3 to 1 would look like [(3, 1)] -> [(2, 2)] -> [(1, 3)]
                while len(stack) > 0 and stack[-1][0] >= curr[j]:
                    count += stack[-1][1]
                    stack.pop()
                left[j] = count
                stack.append((curr[j], count))
            
            stack = [] # reset stack

            # Find all valid end points of rectangle to right of pivot inclusive inclusive of pivot
            # Move from right to left in histogram to see how far right each point can cover to see its
            # terminal smaller value point
            # This is strictly greater than (>) because equal-height bars to the right are counted 
            # independently, preventing double-counting of rectangles.
            for j in range(c - 1, -1, -1):
                count = 1

                # Pop all bars that are strictly greater than current height, and accumulate their counts
                while len(stack) > 0 and stack[-1][0] > curr[j]:
                    count += stack[-1][1]
                    stack.pop()
                right[j] = count
                stack.append((curr[j], count))
            
            # Amount of rectangles for a point = height at curr col * num starting points * num ending points
            for j in range(c):
                res += curr[j] * left[j] * right[j]
        
        return res
            