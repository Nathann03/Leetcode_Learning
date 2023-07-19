"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

"""
Thought process:

Naive/BF:
Knowing anagrams, we can sort each anagram and store a dict with the
key being the sorted anagram and the pair being a list with the corresponding
word unsorted that we can use for later.
Time complexity: m*nlog(n), where m is num of words and the rest is due to sort

Magic:
Looking at the constraints, we have only 26 possible characters that make
up a word. So to avoid the need to sort everything, we can just count 
the letters in each word and make it the key since each anagram will
have the same key and store that in a default dict where the pair is 
the words that have the same key
Time complexity: O(m * n), where m is num of words and n is iterating 
                 thru the word itself.

"""

import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)
        for str in strs:
            # alpha resets every cycle
            alpha = [0] * 26 # Sets up alphabet to use for counting
            
            """
            What is this doing?

            We are accessing the unicode value of each char and subtracting
            it from unicode of "a" so we have the index at which the char
            is in the alphabet, we then access that idx in alpha to 
            increment it so we create the unique key for anagrams
            """
            for char in str:
                alpha[ord(char) - ord("a")] += 1
            
            # inputs alpha as key and appends the assoc string
            # Since its defaultdict, if key DNE, it creates it
            anagrams[tuple(alpha)].append(str)
        return list(anagrams.values())

"""
Quick final thoughts:

Honestly, the Naive/BF solution might be better due to the lack of overhead
needed compared to magic, but magic is really an ingenious solution to
solving anagrams. In a interview, pull out magic since it has faster
run time with larger datasets

"""