# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:
#
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.
#
# # An "if statement" is written by using the if keyword.
# a: int = 330
# b =2000
a=int(input("Please enter your number : "))
# b=int(input("Please enter second number : "))

r = a % 2
if r ==0:
    print("you have entered even number and number was " + str(a))
else:               #using else
# if r ==1:         #using if
    print("you have enterd odd number and number was " + str(a))
# if b > a:
#     print("b is greater than a")
# if b < a:
#     print("a is greater than b")
# if a == b:
#     print("both numbers are equel")
