list = [5, 2, 8, 1, 9, 3, 7, 4, 6, 2]

print(list.count(2))

list.remove(2)
list.remove(2)

list.sort()
list.reverse()
sorted_list = sorted(list)
print(sorted_list)

list.insert(2, 10)
print(list)

sorted_copy = sorted(list)
print("Sorted copy:", sorted_copy)  

list.clear()
print("Cleared list:", list)
