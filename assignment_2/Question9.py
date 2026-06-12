# 9. Write a function: 
# count_frequency(arr) 
# that takes a list as input and prints the frequency of each element. 
# Example: 
# arr = [1, 2, 2, 3, 1, 4, 2] 
#  Output: 
 
#  1 -> 2 times 
# 2 -> 3 times 
# 3 -> 1 time 
# 4 -> 1 time

arr = [1, 2, 2, 3, 1, 4, 2]

def count_frequency(arr):
    for i in set(arr):
        print(i, "->", arr.count(i), "times")
 
count_frequency(arr)
