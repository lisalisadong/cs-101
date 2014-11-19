# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.

def shift(letter):
    return chr((ord(letter) - ord('a') + 1) % 26 + ord('a'))

print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a
