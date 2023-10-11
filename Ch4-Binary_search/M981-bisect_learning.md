##Bisect Learning for Future Use

`bisect` is a Python module that provides functions for binary search and insertion into a sorted sequence. It's a useful tool when you have a sorted list or sequence of values and need to find the insertion point for a new value while maintaining the sorted order, or when you want to locate a value in a sorted sequence efficiently.

The `bisect` module includes two main functions:

1. `bisect.bisect_left(a, x, lo=0, hi=len(a))`: This function finds the index at which you can insert the value `x` into the sorted list `a` such that it remains sorted. It returns the leftmost insertion point, meaning it returns the index of the first element that is greater than or equal to `x`.

2. `bisect.bisect_right(a, x, lo=0, hi=len(a))`: Similar to `bisect_left`, this function also finds the index at which you can insert the value `x` into the sorted list `a` while maintaining the sorted order. However, it returns the rightmost insertion point, which is the index of the first element that is greater than `x`.

These functions use binary search to efficiently locate the insertion point, making them much faster than a linear search when dealing with large sorted sequences.

Here's a brief example of how to use `bisect`:

```python
import bisect

a = [1, 3, 4, 6, 8, 9]
x = 5

# Find the index where x can be inserted while maintaining the sorted order
index = bisect.bisect_left(a, x)
print(index)  # Output: 3 (because 5 should be inserted at index 3 to keep the list sorted)
```

In the context of your `TimeMap` implementation, `bisect` is used to efficiently find the index of a timestamp in the list of timestamps for a given key, allowing you to retrieve the corresponding value associated with that timestamp.