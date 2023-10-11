"""
There is an integer array nums sorted in ascending order 
(with distinct values).

Prior to being passed to your function, nums is possibly 
rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., 
nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 
3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer 
target, return the index of target if it is in nums, or -1 if it 
is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1
"""

"""
Thought process:

Naive:
The obvious easy solution to this problem is just doing a quick
O(n) linear search thru the entire list and see if the target exists
if not return -1

Magic:
So another day another hint, the optimal solution they are searching
for is clearly a binary search, but how do we do it since it is rotated.

Using some of the ideas in min rotated, we know that the list is always
ascending until some inflection point, by having 3 pointers l, r, and mid
we can kinda of see and guess where the inflection point is and
figure out if the wanted value is between the middle point and either
the left of the right depending if we have passed the inflection point
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
        

