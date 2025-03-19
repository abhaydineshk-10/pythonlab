# Initial list
my_list = [5, 3, 8, 6, 7, 2]

# a) Add a new list
new_list = [1, 4, 9]
my_list.extend(new_list)
print("List after adding new list:", my_list)

# b) Sort the list
my_list.sort()
print("List after sorting:", my_list)

# c) Reverse the list
my_list.reverse()
print("List after reversing:", my_list)

# d) Remove an element (identity)
element_to_remove = 6
if element_to_remove in my_list:
    my_list.remove(element_to_remove)
print("List after removing element", element_to_remove, ":", my_list)