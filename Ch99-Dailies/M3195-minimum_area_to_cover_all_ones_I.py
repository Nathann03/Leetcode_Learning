"""
Problem:
Given a 2D binary array `grid`, find a rectangle with horizontal and vertical sides 
with the smallest area such that all the 1's in grid lie inside this rectangle. 

Return the minimum possible area of the rectangle.

Example 1:
Input: grid = [[0,1,0],
               [1,0,1]]
Output: 6
Explanation: 
The smallest rectangle has a height of 2 and a width of 3, so the area = 2 * 3 = 6.

Example 2:
Input: grid = [[1,0],
               [0,0]]
Output: 1
Explanation: 
The smallest rectangle has height 1 and width 1, area = 1 * 1 = 1.

Constraints:
- 1 <= grid.length, grid[i].length <= 1000
- grid[i][j] is either 0 or 1
- There is at least one 1 in grid

---

Thought process:

Naive / Brute Force:
- One could consider checking all possible rectangles and see if they cover all 1's,
  then take the minimum area.
- This would be very inefficient: O((m*n)^2) in the worst case.

Optimized / Intuitive Solution:
- The key insight: The minimal rectangle is simply the bounding box around all 1's.
- To find it, we just need the:
  - Topmost row containing a 1
  - Bottommost row containing a 1
  - Leftmost column containing a 1
  - Rightmost column containing a 1
- Once we have these four boundaries, the area is simply:
    (bottom - top + 1) * (right - left + 1)

Implementation details:
- Initialize top = +inf, bottom = -inf, left = +inf, right = -inf
- Iterate over each cell in the grid:
    - If the cell contains a 1, update the boundaries:
        - top = min(top, r)
        - bottom = max(bottom, r)
        - left = min(left, c)
        - right = max(right, c)
- Finally, compute the area using the bounding rectangle formula.

Time Complexity: O(m * n), where m = number of rows, n = number of columns
Space Complexity: O(1) extra space

"""

# Python implementation with comments
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # Initialize boundaries
        top = float('inf')       # topmost row with a 1
        bottom = float('-inf')   # bottommost row with a 1
        left = float('inf')      # leftmost column with a 1
        right = float('-inf')    # rightmost column with a 1

        # Scan the entire grid to find the bounding box of all 1's
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    # Update the top boundary
                    if r < top:
                        top = r
                    # Update the bottom boundary
                    if r > bottom:
                        bottom = r
                    # Update the left boundary
                    if c < left:
                        left = c
                    # Update the right boundary
                    if c > right:
                        right = c

        # Compute the area of the rectangle using the bounding box
        return (bottom - top + 1) * (right - left + 1)
