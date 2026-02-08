list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

listsquares = []
for i in range(1, len(list) + 1):
    #print(i**2)
    listsquares.append(i**2)
print((listsquares))

even_list = []
for i in range(1, len(list)+1):
    if i % 2 == 0:
        #print (i)
        even_list.append(i)
print(even_list)

list2 = []
for i in range (len(list)):
    if list[i] >5:
        list2.append(list[i]*2)
print(list2)

slist = [str(list[i]) for i in range(len(list))]
print(slist)

tuples = [(list[i], list[i]**2) for i in range(len(list))]
print(tuples)