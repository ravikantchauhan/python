from array import *
roll_stu = array('i', [])
n = int(input("Enter Number of elements: "))
i = 0
j = 0
while i<n:
    roll_stu.append( int( input( "Enter  elements: " ) ) )
    i =i+1
k =len(roll_stu)
while j<k:
    print( roll_stu[j] )
    j =j+1
