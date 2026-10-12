
# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    # Your code here
    if not numbers:
        raise ValueError("The input list is empty.")

    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    return print(max(counts, key=counts.get))

    
test_var = [1, 3, 2, 3, 4, 1, 3, 1, 1]
most_frequent(test_var)
    
    

"""
Time and Space Analysis for problem 1: 
- Best-case: O(N)
- Worst-case: O(N)
- Average-case: O(N)
- Space complexity: O(N)
- Why this approach? I use this approach because it efficiently counts the frequency of each element and finds out the most frequent one.
- Could it be optimized? I think it could be optimized using the library 'collections.Counter'.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    # Your code here
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
test_var_2 = [4, 5, 4, 6, 5, 7]
print(remove_duplicates(test_var_2))


"""
Time and Space Analysis for problem 2:
- Best-case: O(N)
- Worst-case: O(N)
- Average-case: O(N)
- Space complexity: O(1) on the best, O(N) on the rest.
- Why this approach? I use this approach because it efficiently removes duplicates and the use of set allows for the elements to stay in order.
- Could it be optimized? the code could be optimized using a dict since they mantain insertion order.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    # Your code here
    seen = set()
    pairs = []

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs
    
test_var_3 = [1, 2, 3, 4]
print(find_pairs(test_var_3, target=5))
"""
Time and Space Analysis for problem 3:
- Best-case: O(N)
- Worst-case: O(N)
- Average-case: O(N)
- Space complexity: Best case O(1), rest of cases is O(N)
- Why this approach? I think that this approach is the best way of finding all pairs that sum to a target in the most efficient way.
- Could it be optimized? I do not think that this code could be optimized further.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    # Your code here
    capacity = 1
    arr = [None] * capacity
    for i in range(n):
        if i >= capacity:
            capacity *= 2
            new_arr = [None] * capacity
            for t in range(i):
                new_arr[t] = arr[t]
            arr = new_arr
            print(f"Resized array to capacity {capacity}")
        arr[i] = i  
    return arr
test_var_4 = add_n_items(6)
    

"""
Time and Space Analysis for problem 4:
- When do resizes happen? the resizes happen whenever the number of elements matches the current capacity of the array.
- What is the worst-case for a single append? O(N), which happens when a resize occurs.
- What is the amortized time per append overall? O(1), because the cost of resizing is spread out over many appends.
- Space complexity: O(N), where N is the number of elements added, due to the array and its resizing.
- Why does doubling reduce the cost overall? Doubling ensures that the number of resizes grows logarithmically with the number of elements, keeping the amortized cost per append low.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    # Your code here
    output = []
    running_sum = 0
    for num in nums:
        running_sum += num
        output.append(running_sum)
    return output

test_val_5 = [1, 2, 3, 4]
print(running_total(test_val_5))

"""
Time and Space Analysis for problem 5:
- Best-case: O(N)
- Worst-case: O(N)
- Average-case: O(N)
- Space complexity: O(N)
- Why this approach? I thought that this approach is straightforward and efficient for computing running totals.
- Could it be optimized? I do not think that this code could be improved further.
"""


# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

from collections import Counter
def most_frequent(numbers):
    # Your code here
   if not numbers: 
       raise ValueError("The input list is empty.")
   counts = Counter(numbers)
   return max(counts, key=counts.get)

test_var_1_Refactored = [1, 3, 2, 3, 4, 1, 3]
print(most_frequent(test_var_1_Refactored))

'''
I optimized the code by using the counter class from the collections library, which simplifies the counting of elements and makes the finding of the most frequent element more efficient.
'''
