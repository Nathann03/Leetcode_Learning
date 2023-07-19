"""
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.

 
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
IMPORTANT:
Follow up: Your algorithm's time complexity must be better 
than O(n log n), where n is the array's size.

"""


"""
Thought Process:

Naive/BF:
By using the counter method for dictionaries in Collections module, it
will automatically count the occurances of each number in the list. Pairing
with the .most_common() method for count, we create a group of list in
a list for us to use to iterate through the most commmon occurances

Time complexity: O(n log n) -> doesn't work since needs to be O(n)

Magic:
By using the counter method, we can still utilize it due to its O(n)
prowess. However, the change here is instead of using sorting, we can
use something called bucket sort where we will build a n-length array 
of sorts (O(n)) that that uses the frequency as the idx of the list and
inserts (O(n)) the value at that index is a list of the values with that freq.
We iterate (O(n)) right (highest freq) to left (low freq) until we hit k
(Check out picture assoc with this file)

Time complexity: O(n)



"""
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket is n long since list only has n elements
        # Increment because list starts at 0
        bucket = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)

        for num, freq in count.items():
            bucket[freq].append(num)
        
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)

            if len(result) == k:
                return result
