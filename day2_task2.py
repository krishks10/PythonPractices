list = []

list.append(input("Enter an item: "))
list.append(input("Enter another item: "))
list.append(input("Enter one more item: "))

print(list)

print("="*5)

print(len(list))
print(f"first item is: {list[0]}")
print(f"last item is: {list[-1]}")

list.sort()
print("Sorted list:", list)

list.remove(input("Enter an item to remove: "))
print("Updated list:", list)