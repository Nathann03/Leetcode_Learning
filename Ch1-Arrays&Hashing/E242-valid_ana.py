"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

""" 
Thought process:

Naive:
The main idea of this is that all anagrams have the same number of letters
and when sorted should be the same string.

However, if we just sorted it and compared, the big O would be nlogn at best
so how can we improve to n

Magic:
We can use a hash table and utilize its access and add power to make it O(N).
We can create a hash table to count the amt of each char in S
then we can decrement the amt in hash table using char in T
finally, we check if all keys in hash table are 0

Runtime: O(N) bc O(n) + O(n) + O(n)

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        nums = {}

        for char in s:
            if char in nums:
                nums[char] += 1
            else:
                nums[char] = 1
        
        for char in t:
            if char in nums:
                nums[char] -= 1
            else:
                return False
        
        # nums.values creates a list of all values for the keys
        for num in nums.values():
            if num != 0:
                return False
            
        return True

"""
Other solutions:
A cool default dict solution is using the Counter() dict method to
automatically create a dict using a list to count the amount of times
any given item shows up in list.

Runtime: O(n)
"""
import collections 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            one = collections.Counter(s)
            two = collections.Counter(t)
            return one==two