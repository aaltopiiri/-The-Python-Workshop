'''
Fibonacci numbers, the elements of the sequence of numbers
1, 1, 2, 3, 5, 8, 13, 21, …, each of which, after the second,
is the sum of the two previous numbers.
'''
count = True
a = 0
#print(a)
b = 1
while count:
    print(b, end=' ')
    b, a = a + b, b
    if b > 1000:
        break
a+=1