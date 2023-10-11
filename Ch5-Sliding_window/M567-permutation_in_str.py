"""
Given two strings s1 and s2, return true if s2 contains a permutation 
of s1, or false otherwise.

In other words, return true if one of s1's permutations is the 
substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

"""
Thought Process:

Naive/BF:

Magic:
Woohoo its kinda obvious what the solution here is in terms of searching
for a permutation. By using a sliding window and a counter based dict
we can use a fixed window based on how large s1 is and update the counter
for additions and subtractions based on what leaves and enters and then 
compare the two dict to see if they match.

Note: For the solution below, we could use slicing and constantly create
a new counter, but that jacks up the runtime like crazyyyy (~8x) despite 
still being O(n).
"""
from collections import Counter
class Solution:
    def checkInclusion(self, s1:str, s2:str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])

        for i in range(len(s1), len(s2)):
            if s1_counter == s2_counter:
                return True

            left_char = s2[i - len(s1)]
            if s2_counter[left_char] == 1:
                del s2_counter[left_char]
            else:
                s2_counter[left_char] -= 1

            right_char = s2[i]
            s2_counter[right_char] = s2_counter.get(right_char, 0) + 1

        if s1_counter == s2_counter:
            return True

        return False
    
"""
Weird Fucky Solution (From online):
So the idea of this is instead of creating a counter, we just make a list
for all 26 possible characters to reduce space complexity and a bit of
time complexity in theory.

In this approach, we create a window of length n (the length of string s1)
and keep moving the window by one position at a time until we reach the 
end of string s2. In each iteration, we keep track of the frequency of 
characters in the current window and compare it with the frequency of 
characters in string s1. If the two frequency arrays are the same, it 
means that the current window is a permutation of string s1, and we can 
return true.

Time complexity: *O(n + (m-n)26) // where m is the length of s2 string 
                                    and n is the length of s1 string
Space complexity: O(1) // extra space of 26 size is used
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        
        count = [0] * 26
        for i in range(n):
            count[ord(s1[i]) - ord('a')] += 1
            count[ord(s2[i]) - ord('a')] -= 1
        if self.allZeros(count):
            return True
        
        for i in range(n, m):
            count[ord(s2[i]) - ord('a')] -= 1
            count[ord(s2[i - n]) - ord('a')] += 1
            if self.allZeros(count):
                return True
        
        return False
    
    def allZeros(self, count):
        for i in range(26):
            if count[i] != 0:
                return False
        return True

