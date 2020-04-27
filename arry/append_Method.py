from array import *
roll_stu = array('i',[10,20,40,1,3,50])
n = len(roll_stu)
i= 0
while i <n:
    print(roll_stu[i])
    i=i+1
print("print after appand method")
roll_stu.append(80)
roll_stu.append(85)
roll_stu.append(90)
n = len(roll_stu)
i= 0
while i <n:
    print(roll_stu[i])
    i=i+1
print("this is after using for loop")
for k in range(len(roll_stu)):
    print(k,"=" ,roll_stu[k] )