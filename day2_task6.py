numbers = []

print("Enter 5 numbers:")

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print(f"\nYou entered: {numbers}")

for i in numbers:
    print(max(numbers))

for i in numbers:
    print(min(numbers))

print("=" * 20)

sum_numbers = sum(numbers)
print(f"Sum of numbers: {sum_numbers}")

avg_numbers = sum_numbers / len(numbers)
print(f"Average of numbers: {avg_numbers}")