"""
Given a 1-indexed array of integers numbers that is already 
sorted in non-decreasing order, find two numbers such that they add 
up to a specific target number. Let these two numbers be numbers[index1] 
and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, 
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.

IMPORTANT:
Your solution must use only constant extra space.

 
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, 
index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore 
index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore 
index1 = 1, index2 = 2. We return [1, 2].

"""

"""
Thought process:

Another easy 2 pointer problem. SO the idea here is we have a target
that we have to hit, so using two pointers we constantly check if the
values assoc with the pointers equal target.

Since the list is already sorted, we only need to check if the value if
the sum is higher or lower.
if higher, we move the right pointer down so less is being added
if lower, we move the left pointer up so more is added

We do this while left < right

Time complexity: O(n) bc only one pass


Cheater method:
Since we need to use constant space, we cannot create any data types
like dicts, but if we could the solution would be the same as two 
sum from earlier hehe (Check Ch.1 E01)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i, j]
        
        