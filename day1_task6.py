age = int(input("ENTER YOUR AGE: "))
has_license = input("DO YOU HAVE A DRIVING LICENSE? (yes/no): ").lower() == "yes"

if age >=18 and has_license:
    print("You can drive.")

else:
    print("You cannot drive.")

if age >=65 :
    print("You are Senior Citizen.")

if age >=13 and age <20:
    print("You are a Teenager.")

if age >=18 and age <65:
    print("You are an Adult.")

if age >=18:
    print("You are eligible to vote.")