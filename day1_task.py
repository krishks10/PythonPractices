name = str((input("ENTER YOUR NAME: ")))
age = int((input("ENTER YOUR AGE: ")))
height = float((input("ENTER YOUR HEIGHT IN METERS: ")))
language = str((input("ENTER YOUR FAVORITE PROGRAMMING LANGUAGE: ")))
exp = int((input("ENTER YOUR YEARS OF PROGRAMMING EXPERIENCE: ")))
currently_learning = input("ARE YOU CURRENTLY LEARNING TO PYTHON? (yes/no): ").lower() == "yes"

print("=" * 4 + " Personal Information " + "=" * 4)
print(f"Name: {name}")
print(f"Age: {age} years")
print(f"Height: {height} meters")
print(f"Favorite Programming Language: {language}")
print(f"Years of Programming Experience: {exp}")
print(f"Currently Learning Python: {currently_learning}")

print(f"\nType of student_name: {type(name)}")
print(f"Type of student_age: {type(age)}")
print(f"Type of student_height: {type(height)}")