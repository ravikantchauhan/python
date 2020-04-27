# x = "sdddsadjsajdasjdjsd"
# for i in x:
#     print(i)
# for loop with RANGE
# a =range(10)                                        #######print 0 to n-1
# for i in a:
#     print(i)
# b =  range(2,20,3)                                  ##### print range with step
# for i in b:
#     print(i)
#
#####################
# x = "sdddsadjsajdasjdjsd"
# n = len(x)
# for i in range(n):
#     print(i,"=",x[i])
#
###############

x=range(4)
y=range(3)
z =range(2)
for i in x:
    print( "this iner  loop" , x[i] )
    for j in y:
        print ("this is outer loop" ,y[j])
        for k in z:
            print("this sub iner loop", z[k])
