count = True
a, b = 24, 32 #Two numbers
i = 1 #Iterator
while count:
    if (i % a == 0) and (i % b) == 0:
        print("LCM for numbers {} and {} is: {}".format(a, b, i))
        break
    i += 1