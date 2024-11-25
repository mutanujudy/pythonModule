# Step 1: Write favorite movies to a file
with open("movies.txt", "w") as file:
    movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]
    for movie in movies:
        file.write(movie + "\n")  # Write each movie on a new line

print("Movies written to file successfully.")

# Step 2: Read and display the content of the file
print("\nReading file content:")
with open("movies.txt", "r") as file:
    content = file.read()
    print(content)

# Step 3: Append another movie to the file
with open("movies.txt", "a") as file:
    file.write("Avatar\n")

print("New movie appended to file successfully.")

# Step 4: Read and display the updated content
print("\nReading updated file content:")
with open("movies.txt", "r") as file:
    updated_content = file.read()
    print(updated_content)
