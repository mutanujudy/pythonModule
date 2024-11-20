

#Ask the user for the number of integers they want to input
num_of_integers = int(input("How many integers do you want to add to the list? "))

#Initialize an empty list to store the integers
integer_list = []

#Use a loop to get integers from the user
for i in range(num_of_integers):
    number = int(input(f"Enter integer {i + 1}: "))
    integer_list.append(number)

#Compute the sum of the integers in the list
total_sum = sum(integer_list)

#Display the sum
print(f"The sum of the integers {integer_list} is {total_sum}")
