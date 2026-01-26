# Create a list of numbers from 1 to 20
numbers = list(range(1, 21))

print("Numbers:", numbers)

# ---------- Even numbers ----------
print("\nEven numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")

# ---------- Numbers divisible by 3 ----------
print("\n\nNumbers divisible by 3:")
for num in numbers:
    if num % 3 == 0:
        print(num, end=" ")

# ---------- Sum of all numbers ----------
total_sum = 0
for num in numbers:
    total_sum += num

print(f"\n\nSum of all numbers: {total_sum}")

# ---------- Product of all numbers ----------
product = 1
for num in numbers:
    product *= num

print(f"Product of all numbers: {product}")

# ---------- Using enumerate ----------
print("\nNumbers with index:")
for index, value in enumerate(numbers):
    print(f"Index {index} → Value {value}")

# ---------- Range backwards ----------
print("\nNumbers from 10 to 1 (backwards):")
for i in range(10, 0, -1):
    print(i, end=" ")
