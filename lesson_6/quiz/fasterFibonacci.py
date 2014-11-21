#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    i = 0
    result0 = 0
    result1 = 1
    while i < n:                    #for i in range(0, n):
        cache = result1             #result0, result1 = result1, result0 + result1
        result1 = result0 + result1
        result0 = cache
        i = i + 1
    return result0

#shorter:
#def fibonacci(n):
#    result0 = 0
#    result1 = 1
#    for i in range(0, n):
#        result0, result1 = result1, result0 + result1
#    return result0

print fibonacci(36)
#>>> 14930352
