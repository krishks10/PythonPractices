first_name = input("Enter Your First Name: ")
last_name = input("Enter Your Last Name: ")
birth_year = int(input("Enter Your Birth Year: "))
current_year = 2026
favorite_number = float(input("Enter Your Favorite Number: "))

full_name = first_name + " " + last_name
age = current_year - birth_year
fav_no = favorite_number * 2

print("=" * 4 + " User Information " + "=" * 4)
print(f"Full Name: {full_name}")
print(f"Age: {age}")
print(f"Favorite Number: {favorite_number}")
print(f"Favorite Number Doubled: {fav_no}")