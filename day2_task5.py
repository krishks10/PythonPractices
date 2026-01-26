list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range (len(list)):
    if i % 2 == 0:
        print("Even number:", i)
    else:
        print("Odd number:", i)

print("=" * 20)

for i in range (len(list)):
    if i % 2 == 0:
        print(i)

print("=" * 20)

for i in range (len(list)):
    if i % 2 != 0:
        print(i)

for i in range (len(list)):
    if i % 3 == 0:
        print("Divisible by 3:", i)