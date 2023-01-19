
#Write a program to print the following start pattern using the for loop

rows = 7 
  
# Outer loop will print the number of rows  
for i in range(0, rows):  
    # This inner loop will print the stars  
    for j in range(0, i + 1):  
        print("*", end=' ')  
    # Change line after each iteration  
    print(" ")  
# For second pattern  
for i in range(rows + 1, 0, -1):  
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  