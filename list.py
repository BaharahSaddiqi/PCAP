numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.
del numbers[1]
print(numbers[-1])
print(numbers[-4])


print("\nList length:", numbers)  # Printing the list's length.



#wichtig

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)
#





lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)
#




lst = [1,2,3,4]

print(lst)




list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2



print(list_3)
del list_1[0]
del list_2[0]
