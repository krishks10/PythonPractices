from datetime import date
from colorama import Fore, Style, init

init(autoreset=True)

# ---------- INPUT VALIDATION ----------
def get_valid_age():
    while True:
        age = input("Enter your age: ")
        if age.isdigit() and int(age) > 0:
            return int(age)
        print(Fore.RED + "❌ Age must be a positive number!")

def get_valid_email():
    while True:
        email = input("Enter your email: ")
        if "@" in email and "." in email:
            return email
        print(Fore.RED + "❌ Invalid email format!")

def get_valid_phone():
    while True:
        phone = input("Enter your phone number (10 digits): ")
        if phone.isdigit() and len(phone) == 10:
            return phone
        print(Fore.RED + "❌ Phone number must be 10 digits!")

# ---------- USER INPUT ----------
print(Fore.CYAN + "\n✨ Welcome to the Smart User Info Program ✨\n")

name = input("Enter your name: ")
age = get_valid_age()
email = get_valid_email()
phone = get_valid_phone()
country = input("Enter your country: ")
occupation = input("Enter your occupation: ")

# ---------- CALCULATIONS ----------
birth_year = date.today().year - age
days_lived = age * 365  # Approximation

# ---------- OUTPUT ----------
border = "═" * 45

print(Fore.GREEN + f"\n{border}")
print(Fore.YELLOW + "📋 USER SUMMARY")
print(Fore.GREEN + border)

print(f"👤 Name        : {name}")
print(f"🎂 Age         : {age} years")
print(f"📧 Email       : {email}")
print(f"📱 Phone       : {phone}")
print(f"🌍 Country     : {country}")
print(f"💼 Occupation  : {occupation}")
print(f"📅 Birth Year  : {birth_year}")
print(f"⏳ Days Lived  : ~{days_lived} days")

print(Fore.GREEN + border)

# ---------- SAVE TO FILE ----------
with open("user_info.txt", "w") as file:
    file.write(f"""
USER INFORMATION
----------------
Name       : {name}
Age        : {age}
Email      : {email}
Phone      : {phone}
Country    : {country}
Occupation : {occupation}
Birth Year : {birth_year}
Days Lived : {days_lived}
""")

print(Fore.CYAN + "\n💾 Information saved to 'user_info.txt'")
print(Fore.MAGENTA + "🎉 Program completed successfully!\n")
