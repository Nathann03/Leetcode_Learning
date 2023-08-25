## Thoughts and Things to Remember for stacks

The main idea of stack-related LeetCode problems is to use the stack data structure to solve various types of problems efficiently. A stack is a last-in, first-out (LIFO) data structure, where elements are inserted and removed from the same end, known as the "top" of the stack. It follows the Last-In-First-Out (LIFO) principle, meaning that the last element added to the stack is the first one to be removed.

Stacks are useful in solving problems that involve tracking a temporary sequence of elements, managing function calls, parentheses matching, and dealing with nested structures.

# The main characteristics of a stack are:

Push: Adding an element to the top of the stack.
Pop: Removing the top element from the stack.
Peek or Top: Accessing the top element without removing it.
IsEmpty: Checking if the stack is empty.
Size: Determining the number of elements in the stack.

# Some typical types of problems where stack data structure is commonly used in LeetCode include:

Parentheses and Brackets Matching:
Problems related to checking if the parentheses or brackets in an expression are balanced and well-formed. For example:

1. Valid Parentheses
2. Longest Valid Parentheses

# Function Call and Recursion Tracking:
Problems that involve simulating function calls and handling recursive operations using a stack. For example:

1. Evaluate Reverse Polish Notation
2. Binary Tree Inorder Traversal

# Nested Structures:
Problems dealing with nested structures, such as nested lists or nested strings. For example:

Flatten Nested List Iterator
Remove All Adjacent Duplicates in String

# Simplifying Complex Operations:
Using a stack to simplify complex operations or expressions. For example:

Basic Calculator
Remove K Digits
The stack data structure allows for efficient tracking and management of elements, making it a powerful tool to solve various algorithmic and data structure-related problems on LeetCode.

## How to identify if it is a two pointer problem:

1. **Last-in, First-out (LIFO) Behavior:** If the problem involves managing elements based on the last-in, first-out (LIFO) principle, where the last element added is the first to be removed, it suggests a stack might be useful. Stacks are particularly suited for situations where you need to track temporary sequences of elements in reverse order.

2. **Nested Structures or Parentheses Matching:** Problems that deal with nested structures, such as nested parentheses, brackets, or nested lists, often require a stack to ensure proper matching and closing of these structures. If the problem involves checking balanced parentheses or tracking nested elements, a stack is a potential candidate.

3. **Function Call Simulation or Recursion:** When a problem involves simulating function calls or handling recursive operations, you can often use a stack to keep track of the function calls and their state. This approach is useful in problems where you need to process elements or perform operations in a particular order, and a recursive solution might lead to stack overflow.

4. **Backtracking or Undoing Operations:** In problems involving backtracking or undoing certain operations, a stack can be used to store the elements or states that need to be reverted. This allows you to efficiently backtrack and explore different paths.

5. **Parsing and Expression Evaluation:** If the problem requires parsing and evaluating expressions or postfix notation (Reverse Polish Notation), a stack can be helpful to keep track of operators and operands.

6. **Depth-First Search (DFS) or Traversal:** When performing depth-first search or traversal on a graph, tree, or nested data structure, a stack is often used to maintain the current path or nodes to visit.

7. **Simplifying Complex Operations:** Problems that involve simplifying complex operations or expressions by eliminating redundant elements or characters can benefit from using a stack.

8. **Sliding Window Problems:** In some sliding window problems, you can use a stack to efficiently track the window elements and perform operations on the window.

# Techniques to remember

In Python, you can use the built-in `list` data structure to implement a stack. Here are some common stack techniques in Python using the `list` as the underlying data structure:

1. **Initialization:**
   To initialize an empty stack, you can simply create an empty list:
   ```python
   stack = []
   ```

2. **Push:**
   To push (add) an element onto the stack, use the `append()` method of the list:
   ```python
   stack.append(element)
   ```

3. **Pop:**
   To pop (remove and return) the top element from the stack, use the `pop()` method without any argument:
   ```python
   top_element = stack.pop()
   ```

4. **Peek or Top:**
   To get the top element without removing it, you can access the last element of the list using index `-1`:
   ```python
   top_element = stack[-1]
   ```

5. **Check if the Stack is Empty:**
   You can check if the stack is empty by using the truthiness of the list:
   ```python
   if not stack:
       print("Stack is empty.")
   ```

6. **Size of the Stack:**
   You can get the number of elements in the stack using the `len()` function:
   ```python
   size = len(stack)
   ```

7. **Clear the Stack:**
   To clear all elements from the stack, you can use the `clear()` method of the list:
   ```python
   stack.clear()
   ```

Using these techniques, you can easily implement a stack in Python and perform various stack operations. Keep in mind that Python's list is a dynamic array, which allows you to efficiently perform stack operations without worrying about size limitations. However, if you need more advanced features or performance optimizations, you may consider using the `collections.deque` class, which is a double-ended queue and can be used as a stack with similar methods but may offer better performance for certain operations.

-----

`collections.deque` is a class from the Python `collections` module that provides a double-ended queue implementation. It can be used as a stack with efficient `append()` and `pop()` operations from both ends. Here's how you can use `collections.deque` as a stack:

```python
from collections import deque

# Initializing an empty stack using deque
stack = deque()

# Pushing elements onto the stack (from the right side)
stack.append(1)
stack.append(2)
stack.append(3)

# Popping the top element from the stack (from the right side)
top_element = stack.pop()
print("Popped:", top_element)  # Output: Popped: 3

# Peeking the top element without removing it
top_element = stack[-1]
print("Top element:", top_element)  # Output: Top element: 2

# Checking if the stack is empty
if not stack:
    print("Stack is empty.")
else:
    print("Stack is not empty.")  # Output: Stack is not empty.

# Getting the size of the stack
size = len(stack)
print("Size of the stack:", size)  # Output: Size of the stack: 2

# Clearing the stack
stack.clear()

# Checking if the stack is empty after clearing
if not stack:
    print("Stack is empty.")  # Output: Stack is empty.
else:
    print("Stack is not empty.")
```

`collections.deque` provides O(1) time complexity for append and pop operations from both ends, making it an efficient choice for implementing a stack or queue in Python.