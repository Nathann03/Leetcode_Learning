"""
Given an array of integers nums containing n + 1 integers where each 
integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses 
only constant extra space. <== IMPORTANT

Constraints:

1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n    <=== IMPORTANT
All the integers in nums appear only once except for precisely one 
integer which appears two or more times.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
"""

"""
Thought Process:

Naive:
If we disregard the constant extra space bit, the question is pretty easy.
Just iterate through the list and save each value in a set and check if
the value exists in the set. If it does, return true, else once at the
end return false

Magic:
Ah the devil is in the details once again and I am not surprised ughhhh.
If we look at the constraints, we can see that for the highest number, n,
in the list, we will have n+1 numbers in the list. This enables us to do
something pretty cool.

The idea of this solution is what if we treat this as a linked list where
the value is actually the index of the list we want to go next to. That
way if there is a cycle, the duplicate number is the one that points 
to an index twice, so a cycle is generated.

But, all we know how to do is check for cycle detection using floyd's algo.
Well, there is an addition to floyds algo that after we know where the first
pointers meet up. If we return the slow pointer to head and traverse where
the fast ptr moves 1 space (and only 1 space) from orig meet up point 
and the slow pointer moves 1 space from beginning, the next time they 
meet is where the cycle starts AKA the duplicate value in this case!

Crux of this problem: Knowing Floyd's cycle detection algo. Not knowing
this would make this problem pretty imposs to solve IMO.
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        # Note: cannot do:
            # while slow != fast:
            #     slow = nums[slow]
            #     fast = nums[nums[fast]]
        # because it auto fails since slow == fast already at start lmao
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
