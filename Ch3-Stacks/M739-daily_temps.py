"""
Given an array of integers temperatures represents the daily 
temperatures, return an array answer such that answer[i] is the 
number of days you have to wait after the ith day to get a warmer 
temperature. If there is no future day for which this is possible, 
keep answer[i] == 0 instead.

 
Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

"""
Thought Process:

Naive/BF:
The brute force solution to this is for each temp, you just count the
amount of days it takes to find a higher number.
Run time: O(n)

Magic:
The crux of this problem is seeing that it is a stack problem, but 
the stack will have to contain the temperature and the index of said
temp. Also, init a list of all zeros with len of temp list

We iterate through the list and add each temp and idx into stack
and once we move onto the next number, we check if the top of the
stack has the temp that is less than the curr temp. We then go to
the index with the lesser temperature in the zeros list and set the
value to curr idx - less temp idx. We keep doing this to the stack
until the top temp in stack is higher or stack is empty.

"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        final = [0] * len(temperatures)

        for idx, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                prev_temp = stack.pop()
                final[prev_temp[1]] = idx - prev_temp[1]

            stack.append([temperature, idx])
        
        return final