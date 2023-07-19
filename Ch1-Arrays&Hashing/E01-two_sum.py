"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

"""
Thought Process:

Naive/BF:
Using two pointer method, we iterate through each number until
we find the solution and output the two pointer values. Runtime: nlog(n)

Magic:
Lets once again use the magic of hashing to find our solution. Since we 
are given the answer what if we put all values into a hash table with key
being the number and value-pair being index. We can continually search
the next numbers and subtract it from the target and check if it is in 
the hash table.

"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}
        for idx, value in enumerate(nums):
            need = target - value
            if need in seen:
                return [idx, seen[need]]
            else:
                seen[value] = idx