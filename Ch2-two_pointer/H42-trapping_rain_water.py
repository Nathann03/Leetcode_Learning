"""
Given n non-negative integers representing an elevation map where the 
width of each bar is 1, compute how much water it can trap after 
raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""

"""
Thought process:

Naive/BF:
The naive approach I thought of is taking it one layer at a time where we
chop off one level starting from the bottom to the top and count the 
amount of empty space between each "1" since it must be able to trap rain
water.
Runtime: N^k, where k is max height of map

Magic:
The crux of this problem is figuring out the equation to get how much
water is being held in each hole, so the main idea of that is
min(leftmax, rightmax) - current height at i. Using this we can find
the height at each index that water can be held in.

Now using this, how can we solve the problem. Two solutions come to mind
a two pointer problem (difficult, but O(1) space) or using two lists to
hold the lmaxand rmax and any given point by iterating thru the 
height list twice and then going thru it one last time to use the equation
and add up all the results (easier, O(n) space).

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = [0] * n
        rmax = [0] * n
        result = 0

        # Calculate the maximum height from the left side for each index
        max_height = 0
        for i in range(n):
            lmax[i] = max_height
            max_height = max(max_height, height[i])

        # Calculate the maximum height from the right side for each index
        max_height = 0
        for i in range(n - 1, -1, -1):
            rmax[i] = max_height
            max_height = max(max_height, height[i])

        # Calculate trapped water for each index and accumulate the result
        for i in range(n):
            result += max(min(lmax[i], rmax[i]) - height[i], 0)

        return result

    

