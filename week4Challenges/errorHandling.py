try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")


# when not sure which type of error cn occur, use Exception
try:
    with open("some_file.txt", "r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"An error occurred: {e}")

# The finally block runs no matter what happens, ensuring resources are released properly
try:
    file = open("another_file.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed successfully.")

#Combining else and finally
try:
    with open("movies.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully:")
    print(content)
finally:
    print("This will execute no matter what.")

