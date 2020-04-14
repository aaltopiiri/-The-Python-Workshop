for num in range(1,100):
    if num % 2 == 0 and num // 2 != 1:
        continue
    if num % 3 == 0 and num // 3 != 1:
        continue
    if num % 5 == 0 and num // 5 != 1:
        continue
    if num % 7 == 0 and num // 7 != 1:
        continue
    print(num)