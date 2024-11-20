
# Function to get a set of integers from user input
def get_integer_set(prompt):
    # Ask the user to input integers separated by spaces
    numbers = input(prompt)
    # Convert the input string into a set of integers
    return set(map(int, numbers.split()))

#Create two sets from user input
set1 = get_integer_set("Enter integers for the first set (separate using spaces): ")
set2 = get_integer_set("Enter integers for the second set (separate using spaces): ")

#Find the common elements using set intersection
common_elements = set1 & set2  # or  set1.intersection(set2)

#Print the result
print("\nThe common elements between both sets are:", common_elements)
