# Task 1: Read a File and Handle Errors

# Step 1: Try to open and read the file
try:
    with open("sample.txt", "r") as file:
        # Step 2: Print content line by line
        for line in file:
            print(line.strip())   # strip() removes extra newline characters
except FileNotFoundError:
    # Step 3: Handle the error if file does not exist
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    # Handle any other unexpected errors
    print("An unexpected error occurred:", e)
