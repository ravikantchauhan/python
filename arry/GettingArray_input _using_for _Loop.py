from array import *
roll_stu = array('i', [])
n = int(input("Enter Number of elements: "))
for i in range(n):
    roll_stu.append(int(input("Enter  elements: ")))
k =len(roll_stu)
for i in range(k):
    print(roll_stu[i])
