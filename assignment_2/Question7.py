# 7. Create a tuple: 
# data = (5, 10, 15, 20, 25, 30, 35) 
# Write a program to: 
# ○ Count how many elements are divisible by 5 
# ○ Find the sum of all elements 
# ○ Find the average of the tuple

data = (5, 10, 15, 20, 25, 30, 35)
count = 0

for i in data:
    if i % 5 == 0:
        count = count + 1
print(count)


total = sum(data)
print(total)


average = sum(data)/len(data)
print(average)