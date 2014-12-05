# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(i):
    a = 1
    while a < i or a == i:
        print a
        a = a + 1


print_numbers(3)
#>>> 1
#>>> 2
#>>> 3