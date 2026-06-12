# 6. Create a list: 
# arr = [10, 20, 30, 40, 50, 60] 
# Write a function that takes the list as input and returns the list in 
# reverse order without using the reverse() method. 

arr = [10, 20, 30, 40, 50, 60] 
def reverse_list(arr):
    return arr[::-1]

arr = [10, 20, 30, 40, 50, 60]

print("Original List:", arr)
print("Reversed List:", reverse_list(arr))