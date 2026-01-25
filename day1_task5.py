a = int(input("Enter a value: "))
b = int(input("Enter an integer value: "))

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b if b != 0 else "Undefined (division by zero)"
modulo = a % b if b != 0 else "Undefined (modulo by zero)"
exponentiation = a ** b

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulo: {modulo}")
print(f"Exponentiation: {exponentiation}")

print(f"\nType of addition: {type(addition)}")
print(f"Type of division: {type(division)}")
