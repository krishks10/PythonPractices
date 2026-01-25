value = [0, 1, " ", "Hello", [], [1, 2, 3], None, True, False, "False"]

print ("Check Truthy and Falsy values: ")

for item in value:
    if item:
        print(f"{item} is truthy")
    else:
        print(f"{item} is falsy")