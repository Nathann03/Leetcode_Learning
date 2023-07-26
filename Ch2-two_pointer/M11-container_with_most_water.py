"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
 
"""

"""
Thought process:

Naive/BF:
The brute force way of doing this is checking every single possible 
water amount for each line through a loop. The runtime of this is nlog(n).

Magic:
The idea here is using two pointer, but knowing when to move which pointer.
Since we want to maximize the amount of area that we can hold, we want
ideally the highest sides and the widest base, so we always need to move the
pointer with the smallest side so we can maximize the area if there is an
even larger size poss. Fuck small sides fr fr
Time complexity: O(n)
Space complexity: O(1)

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = (min(height[right], height[left]))*(right - left)


            max_area = max(max_area, area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_area

