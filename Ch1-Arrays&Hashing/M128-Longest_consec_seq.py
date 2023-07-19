"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

"""
Thought process:

Naive/BF:
The easy solution to this would be sorting it and then iterating
through while checking if they are consecutive and then holding the
highest number for consec amount.
Time Complexity: O(nlog(n))

Magic:
Using a set, we store all the numbers into the set so we can untilize
its O(1) lookup power. 
Crux of the problem: every string of numbers has a start point, its
                    just the process of finding the start. Prisoner 
                    problem
By iterating through the nums list, we constantly find the longest seq
as it counts up and hold the highest value in a var and use max to
determine longest sequence
Time complexity: O(n)

"""

class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in num_set:
                
                length = 1
                curr = num + 1
                
                while curr in num_set:
                    length += 1
                    curr += 1
                longest = max(longest, length)
        
        return longest