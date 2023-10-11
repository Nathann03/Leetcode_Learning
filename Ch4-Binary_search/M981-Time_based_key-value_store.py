"""
Design a time-based key-value data structure that can store 
multiple values for the same key at different time stamps and 
retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key
"key" with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such 
that set was called previously, with timestamp_prev <= timestamp. 
If there are multiple such values, it returns the value associated 
with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], 
["foo", 4], ["foo", 5]]

Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing. <--- IMP
At most 2 * 105 calls will be made to set and get.
"""

"""
Thought Process:

Naive/BF:
Keep everthing in a 2-d array and just linear search that bitch

Magic:
Well, seeing as the constraints gives us a hint towards the right 
answer, let's see if we can make any modifications to existing stuff
first. Usually for sys design style Qs, we want to use optimal Data
Structures to access, so since we are working with key value pairs,
having a dictionary with O(1) accessing  & setting power is crucial.

In terms of setting and getting, since we are using a dictionary,
we will just set the key given as the key and create a 2-d array
where, idx 0 is the value and idx 1 is the timestamp. Since timestamp
is always increasing using set, the list will always be in order by
timestamp. The issue arises with get as there is no requirement
for get to be the highest value, but has to return either the 
timestamp specified or the pair that is associated with the timestamp
that is less than the one given.

To do this, since it is in order, we just need to do a binary search
of the key pair list to see if timestamp exists or not and return
either the given timestamp or the timestamp that is strictly lower
than the given one.



"""
class TimeMap:

    def __init__(self):
        self.timestamps = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamps:
            self.timestamps[key] = []
        self.timestamps[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        key_list = self.timestamps.get(key, None)

        if not key_list or timestamp < key_list[0][1]:
            return ""
        
        if timestamp > key_list[-1][1]:
            return key_list[-1][0]
        
        left, right = 0, len(key_list) - 1

        while left <= right:
            mid = (left + right) // 2

            if key_list[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        
        return key_list[right][0]
    
# Online answer using bisect
"""
Here's a brief explanation of how it works:

The meta dictionary stores lists of timestamps for each key.
The data dictionary stores lists of values for each key.

When you call the set method, it appends the provided timestamp 
to the meta list and the corresponding value to the data list for 
the given key.

When you call the get method, it uses bisect.bisect to find the 
index of the timestamp in the meta list. This index represents 
the position where the provided timestamp would fit into the sorted 
list of timestamps.
If the index is 0, it means that the provided timestamp is 
earlier than any stored timestamp for the key, so it returns an 
empty string.
Otherwise, it returns the value from the data list at index idx - 1, 
which corresponds to the value associated with the largest 
timestamp_prev that is less than or equal to the given timestamp.
"""
import collections, bisect
class TimeMap:
    def __init__(self):
        self.meta = collections.defaultdict(list)
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.meta[key].append(timestamp)
        self.data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect(self.meta[key], timestamp)
        if idx == 0:
            return ''
        return self.data[key][idx - 1]

