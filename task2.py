# Task 2: Write and Append Data to a File

# Step 1: Take user input and write it to output.txt
user_text = input("Enter some text to write into the file: ")

with open("output.txt", "w") as file:   # "w" mode overwrites the file if it exists
    file.write(user_text + "\n")

print("Data written successfully to output.txt")

# Step 2: Append additional data to the same file
extra_text = input("Enter some text to append into the file: ")

with open("output.txt", "a") as file:   # "a" mode appends data
    file.write(extra_text + "\n")

print("Data appended successfully to output.txt")

# Step 3: Read and display the final content of the file
print("\n--- Final File Content ---")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
