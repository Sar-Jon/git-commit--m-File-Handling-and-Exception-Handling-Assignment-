# Step 1: Ask the user for a filename
filename = input("Enter the filename to read: ")

try:
    # Step 2: Attempt to open the file
    with open(filename, "r") as file:
        content = file.read()

    # Step 3: Modify the content
    modified_content = content.upper()  # Example modification: convert to uppercase

    # Step 4: Write to a new file
    output_filename = "modified_" + filename
    with open(output_filename, "w") as output_file:
        output_file.write(modified_content)

    print(f"Modified content has been written to '{output_filename}'.")
except FileNotFoundError:
    print(f"The file '{filename}' does not exist. Please check the filename and try again.")
except PermissionError:
    print(f"You do not have permission to read the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
