"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence 
and not a substring.

"""

"""
Thought Process:

Naive:
The easy obivious naive solution to this is going each character one by
one and for each char iterate thru the next characters until we get a 
repeat then save the length of the char.

Magic (my own):
So the main idea of this is that this is a substring problem, which usually
is a sliding window problem. The crux of this problem is that we need to
keep track of what was seen in the window so we know that it is unique. 
We keep increasing the window since we know that whatever longest substr
the comes next must be within the window when we either shift it or 
increment it to add to the window. Therefore, the window evolves with 
the longest substr it has seen and compares the size with the next slice

Issue: This is O(nlog n) so not optimal for sliding window

Magic (w/ some help):
Keeping the idea of seen, what if we keep track of where the last occurs
so that if we do see it, we only need to check if it is in window before
expanding. If it is, we just move left ptr to seen[letter] + 1. The kinda
brain fuck is that we keep this old info of last seen since we are already
checking if it is in the range.

This is O(n) because we always want to be ingesting something and not
waiting on menial tasks before increasing.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        result = 0
        for right in range(len(s)):
            if s[right] not in seen:
                result = max(result, right - left + 1)
            else:
                if seen.get(s[right]) < left:
                    result = max(result, right - left + 1)
                else:
                    left = seen[s[right]] + 1
            seen[s[right]] = right
        
        return result
            
