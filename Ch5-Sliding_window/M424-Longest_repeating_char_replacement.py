"""
You are given a string s and an integer k. You can choose any character 
of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter 
you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
"""

"""
Thought Process:

Naive:
A brute force solution to this problem involves a nested loop approach to 
iterate through all possible substrings of the given string s. For each 
substring, the algorithm calculates the frequency of each character, 
identifies the character with the highest frequency, and calculates the 
number of characters that need to be changed to make the substring 
consist of the same character throughout. If the number of required 
operations is within the allowed limit k, it updates a max_length 
variable to store the maximum length of such substrings encountered 
so far. After iterating through all substrings, the algorithm returns 
the value of max_length as the result. However, this brute force 
approach has a time complexity of O(n^3).

Magic:
Ok, so I think I need to solidify my idea of sliding window. So this 
window isn't exactly static in terms of what it is reading and can be
adjusted and expanded/contracted depending on certain conditions. This
can be powerful if we just take time to accept that the most elegant sol
from LC doesn't use left ptr bc its being stupid and doesn't want to
accept the fact that it we use left ptr to adjust the window, at worse
it is O(2n) which is still O(n) compared to their trickery to keep it O(1*n)

So in terms of this question, initializing the left and right ptr at
the begininng, we can create a window where we ingest each character
and keep track of the highest occuring character. After each ingestion
we do the len(window) - highest occurance, if it is higher than k, we 
use the left ptr to shrink the window and keep track of the occurrances
still. Once it is less than or equal to k, we can keep ingesting.

The crux of this problem is realizing that we are using the same principle
as M3-Longest_substring where the window is already the max length and
we will always need to exceed that length, so whatever substr we were trying
to find will always have to exceed that length so we just keep moving on
until the offending factor is out or we get to the end of the line.
Therefore, the max length of the string is always stored in len of window

The other crux is realizing we don't always need to keep track what char
string we are keeping with (aka all A's) since every letter we ingest, 
we can just store the current max frequency and other letters may start
taking over once we ingest more so it is more realistic to do it this way.
This helps with the over k calculation as we make the window 1 smaller so
there is more space to work with. We also don't have to worry if the 
max frequency changes after the shrinking since the next overtaking char
needs to be the max frequency originally if it wants to increase the window
size.

Learnings:
A lot of the time it seems like sliding window answers for longest is 
found within the length of the window. Also, breaking the idea that the
window is fixed needs to be addressed.

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        max_len = 0
        freq_dict = {}

        for right in range(len(s)):
            char = s[right]
            freq_dict[char] = freq_dict.get(char, 0) + 1

            max_freq = max(max_freq, freq_dict[char])

            if right - left + 1 - max_freq > k:
                freq_dict[s[left]] = freq_dict.get(s[left], 0) - 1
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len



