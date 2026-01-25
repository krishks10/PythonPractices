#Collecting user information

first_name = str((input("ENTER YOUR FIRST NAME: ")))
last_name = str((input("ENTER YOUR LAST NAME: ")))

full_name = first_name + " " + last_name

user_age = int((input("ENTER YOUR AGE: ")))
email = str((input("ENTER YOUR EMAIL ADDRESS: ")))
phone_number = str((input("ENTER YOUR PHONE NUMBER: ")))
country = str((input("ENTER YOUR COUNTRY: ")))
known_languages = str((input("ENTER LANGUAGES YOU KNOW (comma separated): ")))
exp = int((input("ENTER YOUR YEARS OF PROGRAMMING EXPERIENCE: ")))
is_student = input("ARE YOU A STUDENT? (yes/no): ").lower() == "yes"
currently_learning = input("ARE YOU CURRENTLY LEARNING PYTHON? (yes/no): ").lower() == "yes"

# Calculation

birth_year = int(input("ENTER YOUR BIRTH YEAR: "))
current_year = 2024

calculated_age = current_year - birth_year

average_exp_per_language = exp / len(known_languages.split(',')) if known_languages else 0

print("================= Welcome To User Info Collector! ================")
print(f"Full Name: {full_name}")
print(f"Age: {user_age} (Calculated Age from Birth Year: {calculated_age})")
print(f"Email Address: {email}")
print(f"Phone Number: {phone_number}")
print(f"Country: {country}")
print(f"Known Languages: {known_languages}")
print(f"Years of Programming Experience: {exp}")
print(f"Average Experience per Language: {average_exp_per_language:.2f} years")
print(f"Is Student: {'Yes' if is_student else 'No'}")
print(f"Currently Learning Python: {'Yes' if currently_learning else 'No'}")