# Print the following pattern
# Write a program to use for loop to print the following reverse number pattern

rows = int(input("Enter the number of rows: "))  
for i in range(0, rows + 1):  
    # inner loop for decrement in i values  
    for j in range(rows - i, 0, -1):  
        print(j, end=' ')  
    print()  