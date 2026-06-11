#2.a Python program to create three variables: 
# • name  
# • age  
# • city 
Name = "Apoorva"
Age = 20
City = "Pilani"
print("Name: " , Name)
print("Age: " , Age)
print("City: " , City)


#3.a Python program that: 
# Takes a user's name as input.  
# Prints the name in uppercase.  
# Prints the total number of characters in the name.
name = input("Enter your name: ")
print(name.upper())
print(len(name))


#4.five commonly used string methods in Python
name = "apoorva"
print(name.upper())
print(name.lower())
print(name.capitalize())
intro = "I love Java"
print(intro.replace("Java","Python"))
text = "Python "
print(text.strip())

#5.Create a list containing the names of five fruits. 
# • Print the complete list.  
# • Print the first and last element.  
# • Print the total number of items in the list. 
lst = ["apple" , "banana" , "grapes" , "orange" , "mango"]
print(lst)
print(lst[0])
print(lst[-1])
print(len(lst))

#6.a Python program to: 
# • Create a list of numbers [10, 20, 30, 40, 50]  
# • Add 60 to the list.  
# • Remove 20 from the list.  
# • Print the updated list. 
lst1 = [10 , 20 , 30 , 40 , 50]
lst1.append(60)
print(lst1)
lst1.remove(20)
print(lst1)


