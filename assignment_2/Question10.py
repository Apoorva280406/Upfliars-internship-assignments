# 10. Write a function: 
# find_duplicates(arr) 
# that takes a list as input and prints all duplicate elements present in 
# the list. 
#            Example: 
# arr = [10, 20, 30, 20, 40, 10, 50, 30] 
#             Output: 
#            Duplicate elements are: 
# 10 
# 20 
# 30


arr = [10, 20, 30, 20, 40, 10, 50, 30]

def find_duplicates(arr):
    print("Duplicate elements are:---")
    
    for i in set(arr):
        if arr.count(i) > 1:
            print(i)

arr = [10, 20, 30, 20, 40, 10, 50, 30]

find_duplicates(arr)