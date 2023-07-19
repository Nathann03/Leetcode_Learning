"""
Given an integer array nums, return an array answer such 
that answer[i] is equal to the product of all the elements 
of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed 
to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time 
and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed 
to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity 
analysis.)
"""

"""
Thought Process:
Since it is O(n) time, we must be using some sort of hashing and/or
accessing array to solve this problem.

Naive/BF:
Using division, we could multiply the entire list and divide each number
from the total to get an O(N) solution, but that is illegal RIP

Magic:
We could create a premade array with len(list) 1s, so we can utilize
its O(1) accessing/setting power. The cool idea here is using the idea
of prefix and postfix where we calculate all the values from left 
to right in the prefix so we calculate all possibilites of numbers
before the given number and do it vice versa since multiplying the
prefix * postfix should give you the solution. Therefore, by using
one array, we just iterate once forwards and once back to get prefix
and postfix. Crux of problem is realizing you need to break up the
problem into two parts since there is a separator.

Time complexity: O(n) + O(n) = O(n)

Check out picture assoc w/ it. We only want the before and after of
each value since that contains the added value of prefix and postfix
together before we multiply in the value that we want to exclude.


"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = [1] * len(nums)
       
        #Need to init prefix & postfix since we use it for first term
        prefix = 1

        for i in range(len(nums)):
            solution[i] = prefix
            prefix *= nums[i]

        postfix = 1

        # Note: stops at -1 since we want to include 0 (start, stop, step)
        for i in range(len(nums) - 1, -1, -1):
            # Does solution first since this is after the index
            solution[i] *= postfix
            postfix *= nums[i]
        
        return solution

