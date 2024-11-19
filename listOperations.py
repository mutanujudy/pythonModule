# Step 1: Create an empty list
my_list = []

# Step 2: Append the elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Step 3: Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)
print(my_list)

# Step 4: Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print(my_list)

# Step 5: Remove the last element from my_list
my_list.pop(-1)
print(my_list)

# Step 6: Sort my_list in ascending order
my_list.sort(reverse=False)
print(my_list)

# Step 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("The index of 30 in my_list is:", index_of_30)
