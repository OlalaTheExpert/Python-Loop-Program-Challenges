#  Print list in reverse order using a loop
# Given: list1 = [10, 20, 30, 40, 50]

#Initialize array     
list1 = [10, 20, 30, 40, 50];    
print("Original array: ");    
for i in range(0, len(list1)):    
    print(list1[i]),     
print("Array in reverse order: ");    
#Loop through the array in reverse order    
for i in range(len(list1)-1, -1, -1):     
    print(list1[i]),     