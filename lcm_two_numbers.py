'''
In arithmetic and number theory, the least common multiple, lowest common multiple,
or smallest common multiple of two integers a and b, usually denoted by LCM(a, b),
is the smallest positive integer that is divisible by both a and b.[1] Since division
of integers by zero is undefined, this definition has meaning only if a and b are both
different from zero.
'''
count = True
print("Input first positive integer number from 1 to 100")
a = int(input()) #First number for example 37
print("Input second positive integer number from 1 to 100")
b = int(input()) #Second number for example 53
i = 1 #Iterator
while count:
    if (i % a == 0) and (i % b) == 0:
        print("LCM for numbers {} and {} is: {}".format(a, b, i))
        break
    i += 1