"""
A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters 
include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing 
non-alphanumeric characters.Since an empty string reads 
the same forward and backward, it is a palindrome.

"""

"""
Thought process:

Easy 2 pointer question, one pointer starts at 0 and the other 
starts at n-1. We skip over everything that is not alphanumeric
and check if each pointer is the same and increment if it is.
Time complexity: O(n)
Space complexity: O(1)

Note: cheat [str] == str[::-1] doesnt work here since it has other
chars to disregard. and takes O(n) space which isn't optimal
Time complexity: O(n)
Space complexity: O(n)

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) -1
        while i < j:
            if not(s[i].isalnum()):
                i += 1
            elif not(s[j].isalnum()):
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        
        return True