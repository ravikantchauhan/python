import array
roll_list: object =array.array("i",[10,20,40,1,3,50])
# print(roll_list[3])
n: int = len(roll_list)
for k in range(n):
    print(k,"=" ,roll_list[k])