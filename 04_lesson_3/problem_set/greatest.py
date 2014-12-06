# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(p):
    result = 0
    for e in p:
        result = max(result, e)
    return result


print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
