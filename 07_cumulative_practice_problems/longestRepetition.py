# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

def longest_repetition(elements):
    count, count_cache = 0, 0
    longest, longest_cache = None, None
    for e in elements:
        if e == longest:
            count = count + 1
        if e != longest and e == longest_cache:
            count_cache = count_cache + 1
        if e != longest and e != longest_cache:
            longest_cache = e
            count_cache = 1
        if count < count_cache:
            longest = longest_cache
            count = count_cache
    return longest


#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None
