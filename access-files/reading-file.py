import os

# Check if the file exists
file_path = 'hello.txt'

if os.path.exists(file_path):
    
    # Open the file in read mode
    file = open(file_path, 'r')
    
    # Read the content of the file
    content = file.read()
    
    print(content)  # Display the content
    # Close the file
    file.close()
else:
    print("File does not exist")
