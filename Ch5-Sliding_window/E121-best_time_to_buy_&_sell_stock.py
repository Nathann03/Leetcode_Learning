"""
You are given an array prices where prices[i] is the price of a given 
stock on the ith day.

You want to maximize your profit by choosing a single day to buy one 
stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

 
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

"""
Thought Process:

Naive:
The somewhat obvious brute force solution to this is going one by one
and checking all possible values when selling for profit, which ends
up being nlog(n)

Magic:
First Sliding window problem woo! Well the idea of a sliding window
is kinda of a two pointer problem but both pointers start at 0 and 1
respectively and slide based on certain criteria and based on this sliding
we perform actions.

For example if we wanted the sum of a long sublist, if we slid the range
the non sliding window thought is that we have to recalculate everything
which is tedious and slows down the process by n, so why don't we just
subtract the value we leave behind and add the incoming value. This keeps
it O(n) if we are iterating thru all x length sublists. Therefore the
adding and subtracting is one of the criteria we base it on to keep it
moving fast inside the sublist. It is always good to note that if you
were trying to keep a max, the window always iterates thru since it needs
to see all values so remember to set a max place holder

In terms of best time to buy and sell, for maxiumum profits, we want the
largest value at the front and the smallest value at the end. Therefore,
sliding window would be optimal since we need to make sure that the ptrs
don't cross each other and keep sliding along the list based on if we 
encounter a big number or small number.

Main Idea:
If ingested value is less than left most value, set that value as left
and move right 1 if possible. Else, keep moving right and checking value
to see if max

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            profit = prices[r] - prices[l]

            if prices[l] < prices[r]:
                max_profit = max(max_profit, profit)
            else:
                l = r
            
            r += 1

        return max_profit