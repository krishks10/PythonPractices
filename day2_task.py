age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
    print("Child")

elif age >= 13 and age <= 19:
    print("Teenager")

elif age >=20 and age <=64:
    print("Adult")

elif age >=65:
    print("Senior")

has_license = input("Do You have Driver's License (yes/no): ").lower() == 'yes'

if age >= 18 and has_license:
    print("You can drive.")

if age >= 18:
    print("You are eligible to vote.")  

if age >= 21:
    print("You can Drink")

if age >= 65:
    print("You are a Senior Citizen.")
