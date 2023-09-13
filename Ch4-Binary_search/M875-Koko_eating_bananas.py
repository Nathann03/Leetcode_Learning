"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109

IMP: The amount of hours before guard coems back is always greater or equal to len(piles)
"""

"""
Thought process:

Naive:

So the main idea of this problem is finding the problem space. Since the amount
of time the guards will always come back is higher or equal to len(piles), that
means that the fastest that koko will need to eat is max(piles) since she
would devour each pile once. Therefore the space we would need to search is
1 <= koko eating speed <= max(piles)
Knowing this, we can linear search O(n) through each value to check if it is feasable
to eat this fast and still make it before the guards come back

Magic:

Well, since we know the non-optimal solution is a ordered list, the faster solution is more
likely to be done using binary search. So by binary search, we could use that list to search
for the feasable value to the solution. If middle is feasable, the l = middle, h = high,
else, h = middle, l = low

Crux of problem:
Checking feasability:
how to check if feasable: 
Iterate thru the piles list and check how many hours it takes to eat all the piles
formula == sum(ceil(pile #n/ eating speed)) for pile in piles

 

"""
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasable(speed):
            return sum(math.ceil(pile / speed) for pile in piles) <= h
        
        left, right = 1, max(piles)

        while left < right:
            mid = (right + left) // 2
            if feasable(mid):
                right = mid
            else:
                left = mid + 1

        return left



