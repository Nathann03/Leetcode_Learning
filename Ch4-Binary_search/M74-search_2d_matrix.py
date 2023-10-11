"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

"""
Thought Process:

Naive:
Linear search thru entire matrix

Magic:
Since the matrix is sorted by way of column -> row, we can assume
the best solution is binary search, but how do we do it in 3-d

If we just take it as a 1-d matrix where we just keep finding the middle
we just do binary search.
The crux of the problem is accessing each value as you half, so the
general idea is to choose for column, it is idx % num of columns, and 
to choose the row (i.e. the submatrix), it is idx // num of cols.

matrix[idx // amt cols][idx % amt cols]

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        r, c = len(matrix), len(matrix[0])
        left, right = 0, r*c - 1 # -1 damn it!!!

        while left <= right:
            mid = (right + left) // 2

            if matrix[mid // c][mid % c] == target:
                return True
            elif matrix[mid // c][mid % c] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        return False
