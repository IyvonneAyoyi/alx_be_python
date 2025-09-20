# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop for columns
    for col in range(size):
# Print stars without moving to new line       
        print("*", end="")  
# Move to next line after each row        
    print()  
    row += 1