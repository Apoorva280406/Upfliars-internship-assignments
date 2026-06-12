# 5. Create a dictionary: 
# 5. Create a dictionary: 
# student = {"name":"Kriti", "age":20, "course":"Python"} 
# Print: 
# ● Complete dictionary  
# ● Student name  
# ● Student age  
# ● Student course Create a list: 
# numbers = [12, 45, 7, 23, 56, 89, 34] 
# Write a program to find: 
# o Largest element 
# o Second largest element 
# o Smallest element

student = {
    "name":"Kriti",
    "age":20,
    "course":"Python"
    }
print(student) 
print(student.get('name'))
print(student.get('age'))

numbers = [12, 45, 7, 23, 56, 89, 34]
print(max(numbers))
numbers.sort()
print(numbers[-2])
print(min(numbers))
