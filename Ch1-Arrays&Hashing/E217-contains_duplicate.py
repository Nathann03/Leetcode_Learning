'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

'''

# My solution is iterating thru each num and checking if it is in the set
# Else, if not add to set
# Time complexity O(N)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False
    
