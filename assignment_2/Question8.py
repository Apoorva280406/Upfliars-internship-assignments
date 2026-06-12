# 8. Create a dictionary: 
# students = { 
# "Aman": 78, 
# "Riya": 92, 
# "Kriti": 88, 
# "Rahul": 95 
# } 
# Write a program to: 
# ○ Find the student with the highest marks 
# ○ Find the student with the lowest marks 
# ○ Print only the students who scored more than 85 marks

students = { 
 "Aman": 78, 
 "Riya": 92, 
 "Kriti": 88, 
 "Rahul": 95 
 } 

print(max(students.values()))
print(min(students.values()))

for i in students:
    if students[i]>85:
     print(i)
    

