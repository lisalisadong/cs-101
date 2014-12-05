# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.


def bigger(number1, number2):
    if number1 < number2:
        number1 = number2
    return number1


print bigger(2,7)
#>>> 7

print bigger(3,2)
#>>> 3

print bigger(3,3)
#>>> 3