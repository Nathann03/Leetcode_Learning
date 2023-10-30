"""
Design a data structure that follows the constraints of a Least Recently 
Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, 
otherwise return -1.

void put(int key, int value) Update the value of the key if the 
key exists. Otherwise, add the key-value pair to the cache. If the 
number of keys exceeds the capacity from this operation, evict the 
least recently used key.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 10^5 calls will be made to get and put.

Note: While it doesn't outright say it, for LRU cache, it should be 
assumed that the keys are unique
"""

"""
Thought Process:

Naive:
If we disregard the O(1) requirement for each function, how would we solve
this problem?

Given that it is an LRU Cache, the system/OS solution to this is creating
a df with a flag to check if it is LRU. However, since we know this is 
not the OS implementation, what is an easy way of doing this?

As a brute force method, we can use a list as a stack where it follows 
last in first out, but we keep the length to be at most the size of capacity
The list would hold a tuple with the format (key, value)

For the get method, we just iterate through the list and find the 
requested key. If we do find it, we pop that from the list and add
it to the front of the list.

For the put method, we would push the value to the front of the list
and check if the list length > capacity. If it is, we just pop the last
value in the list because it was the least recently used.

---

Magic:
Knowing the OS Solution uses nodes and we need to keep this within O(1)
range for the solution, this gives us a bit of a hint for the solution.
What if instead we used a doubly linked list instead of a regular list.

But why you may ask?
Well, if you may have forgotten like me, the runtime for removing an 
element in the middle of the list and shifting over the remaining items 
is actually O(n), which breaks our O(1) rule.

By using a doubly linked list, we can avoid that as we just join the prev
and next node together. However, the issue now arises is that how do we
access a middle node without iterating thru the entire LL O(N) style?
Well, lets use a hashmap where we can hash the key and attach the node
associated with the key within the LL. 

For the get method, we would check the dict if the key exists. If it does,
delete the node from the DLL and add it back to the front. Then
return the value of the key. If it does not exist, return 0

For the put method, we would check if the key exists in the dict. If it
does, update the value of the node in the DLL and remove it from the DLL
then put it back in the front of the DLL. If DNE, then create a node
to add to the DLL in the front and add it to the dict for hashing. 
Then check if the DLL length (separate var to check) is greater than
capacity. If it is, evict LRU key (aka last key in DLL) and remove it
from the dict. 


"""
class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None   
        

class LRUCache:

    def __init__(self, capacity: int):
        self.keypair = dict()
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def push_node(self, node):
        head_next = self.head.next 
        self.head.next = node 
        node.prev = self.head 
        node.next = head_next 
        head_next.prev = node
    
    def remove_lru(self):
        if len(self.keypair) == 0:
            return

        tail_node = self.tail.prev
        del self.keypair[tail_node.key]
        self.remove_node(tail_node)

    def get(self, key: int) -> int:
        if key in self.keypair:
            node = self.keypair[key]
            self.remove_node(node)
            self.push_node(node)
            return node.value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.keypair:
            node = self.keypair[key]
            self.remove_node(node)
            self.push_node(node)
            node.value = value
        else:
            node = Node(key, value)
            self.keypair[key] = node
            self.push_node(node)

            if len(self.keypair) > self.capacity:
                self.remove_lru()
        


"""
Magic 2.0 Cheese solution:
Once in a blue moon there is an amazing cheese solution that we get to 
utilize if we ever run into this problem and not wanna deal with all the
BS we just coded above.

In Python Collections import, there is a cool thing called OrderedDict
that has the power of a dict but is ordered. he OrderedDict keeps the 
order of elements added to the dictionary. This attribute can be used to 
keep track of the least recently used value order.

It also has the methods of a list where we can move to end and pop in 
O(1) time which is soooo cringeeee. Guess how this is implemented however?
With some time saving mods, it is implemented the same way as the above
solution so WOW we did the same thing, but slightly worse bc python research
is better lmao.

INSANELY CRINGE LMAOOOO
"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
			# if we touch a key to return its value, we need to add it 
			# to the end of the least recently used items in our cache
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # check if key already exists - if yes, move item to end and update the value
        if key in self.cache:
            self.cache.move_to_end(key)
        # if cache is full, remove least recent item (first value in OrderedDict)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
		# update/add value
        self.cache[key] = value