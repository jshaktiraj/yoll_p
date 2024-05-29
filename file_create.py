import os

# Directory where you want to create the text files
directory_path = "./sample_dir2"  # Change this to your desired directory path

# Create the directory if it doesn't exist
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Create 100 text files in the directory
for i in range(1, 101):
    file_name = f"file_{i}.txt"
    file_path = os.path.join(directory_path, file_name)
    
    # Create and write content to the text file
    with open(file_path, 'w') as file:
        file.write(f"This is text file {i}")

print("100 text files created successfully.")
