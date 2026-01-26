numbers = []

# ---------- INPUT ----------
print("Enter 5 numbers:")
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# ---------- FIND MAX, MIN, SUM ----------
maximum = numbers[0]
minimum = numbers[0]
total = 0

for num in numbers:
    total += num

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

average = total / len(numbers)

# ---------- CATEGORIZATION ----------
categories = []

for num in numbers:
    if num >= 80:
        categories.append("High")
    elif num >= 50:
        categories.append("Medium")
    else:
        categories.append("Low")

# ---------- STORE RESULTS IN DICTIONARY ----------
results = {
    "max": maximum,
    "min": minimum,
    "average": average,
    "categories": categories
}

# ---------- DISPLAY OUTPUT ----------
print("\n📊 Results Summary")
print("─" * 30)
print(f"Maximum   : {results['max']}")
print(f"Minimum   : {results['min']}")
print(f"Average   : {results['average']:.2f}")
print("Categories:")

for i, category in enumerate(results["categories"]):
    print(f"  Number {numbers[i]} → {category}")
