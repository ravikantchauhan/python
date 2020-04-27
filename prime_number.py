#  prime numbers
# a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11).
# "prime numbers are very useful in cryptography"

num = 10

for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        # break
else:
    print("Prime")